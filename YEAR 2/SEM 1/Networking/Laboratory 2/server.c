#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <netinet/ip.h>
#include <arpa/inet.h>
#include <pthread.h>
#include <stdbool.h>
#include <unistd.h>

#define PORT 1337
#define BACKLOG_MAX 50
#define MAX_THREADS 50
#define MAX_DATA_LEN 500

void error(char *msg) {
	perror(msg);
	exit(0xDEAD);
}

void *client_thread(void *clientSocket) {
	int cSocket = (int)clientSocket;

	uint16_t dataLen = 0;
	ssize_t received = 0;
	
	received = recv(cSocket,&dataLen,sizeof(dataLen),0);

	if(received == - 1) {
		close(cSocket);
		error("[Server]: Could not get data length!\n");
	}

	// convert to host order
	dataLen = ntohs(dataLen);

	if(dataLen > MAX_DATA_LEN) {
		close(cSocket);
		error("[Server]: Reached maximum data length!\n");
	}
	
	// get the actual data
	int32_t data[dataLen];
	received = recv(cSocket,data,sizeof(data),0);
	
	if( received == -1 ) {
		close(cSocket);
		error("[Server]: Could not received data.\n");
	}
	
	int32_t sum = 0;

	for(int i = 0; i < dataLen; i++) {
		sum+=ntohl(data[i]);
	}

	// now we send the data
	// but first convert to network order
	sum = htonl(sum);

	ssize_t sent = send(cSocket,&sum,sizeof(sum),0);

	if( sent == -1 ) {
		close(cSocket);
		error("[Server]: Could not send sum data!\n");
	}

	close(cSocket);
	
	return NULL;
}

int main(void) {
	int sock = socket(AF_INET,SOCK_STREAM,0);

	if( sock == -1) {
		error("[Server]: Unable to create socket!\n");
	}
	// set-up server socket
	struct sockaddr_in server;
	memset(&server,0,sizeof(struct sockaddr_in));
	server.sin_family = AF_INET;
	server.sin_port = htons(PORT);
	server.sin_addr.s_addr = INADDR_ANY;
	socklen_t serverLen = sizeof(struct sockaddr_in);
	
	// bind server
	if( bind(sock,(struct sockaddr*)&server,serverLen) == -1 ){
		close(sock);
		error("[Server]: Could not bind socket!\n");
	}

	printf("Server listening on: %d\n",PORT);

	int res = listen(sock,BACKLOG_MAX);
	
	if( res == -1) {
		close(sock);
		error("[Server]: cannot listen!\n");
	}
		
	while(true) {
		struct sockaddr_in client;
		memset(&client,0,sizeof(struct sockaddr_in));
		int cLen = sizeof(struct sockaddr_in);
		int cSocket = accept(sock,(struct sockaddr*)&client,&cLen);

		if( cSocket == -1) {
			close(sock);
			error("[Server]: Could not accept client!\n");
		}
		
		uint32_t port= ntohs(client.sin_port);
		char *address = inet_ntoa(client.sin_addr);
		printf("[Server]: Client connected %s::%d\n",address,port);

		pthread_t cThread;
		pthread_create(&cThread,NULL,client_thread,(void*)cSocket);
	}


	return 0;
}
