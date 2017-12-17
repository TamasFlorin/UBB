#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <netinet/ip.h>
#include <arpa/inet.h>
#include <pthread.h>
#include <unistd.h>

#define PORT 1337
#define MAX_BUFFER_LEN 100

void error(char *msg) {
	perror(msg);
	exit(0xDEAD);
}

struct Request
{
	struct sockaddr_in clientSocket;
	int sock;
	int dataLen;
	int clientLen;
};

int currentPort = PORT + 1;
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;

void *handle_client(void *data) {
	struct Request *r = (struct Request*)data;
	int newSocket = socket(AF_INET,SOCK_DGRAM,0);	
	
	pthread_mutex_lock(&lock);
	struct sockaddr_in addr;
	addr.sin_family = AF_INET;
	addr.sin_port = htons(currentPort);
	addr.sin_addr.s_addr = inet_addr("0.0.0.0");
	
	while( bind(newSocket,(struct sockaddr*)&addr,sizeof(struct sockaddr_in)) == -1 ) {
		currentPort = currentPort + 1;
		addr.sin_port = htons(currentPort);
	}
	printf("Found free port: %d\n",currentPort);

	currentPort = currentPort + 1;
	
	pthread_mutex_unlock(&lock);
	
	int len = sizeof(addr);
	int port = addr.sin_port;
	int sentPort = sendto(r->sock,&port,sizeof(int),0,(struct sockaddr*)&r->clientSocket,r->clientLen);
	
	if( sentPort == -1) {
		error("Could not send port to client!\n");
	}

	int buffer[MAX_BUFFER_LEN];
	
	int received = recvfrom(newSocket,buffer,MAX_BUFFER_LEN,0,(struct sockaddr*)&addr,&len);

	if( received == -1) {
		perror("Could not receive data from client...\n");
	}

	int dataLen = ntohs(r->dataLen);
	int sum = 0;

	for(int i = 0; i < dataLen; i++) {
		sum+=ntohs(buffer[i]);
	}
	
	int cLen = r->clientLen;

	sum = htons(sum);	
	
	int sent = sendto(newSocket,&sum,sizeof(int),0,(struct sockaddr*)&addr,len);
	
	if(sent == -1) {
		error("Could not send sum to client!\n");
	}

	free(r);
	close(newSocket);

	return NULL;
}

int main(void) {
	int sock = socket(AF_INET,SOCK_DGRAM,0);

	if( sock == -1 ) {
		error("[Server]: Unable to create socket!\n");
	}

	struct sockaddr_in addr;
	addr.sin_family = AF_INET;
	addr.sin_port = htons(PORT);
	addr.sin_addr.s_addr = inet_addr("0.0.0.0");

	// now bind this socket
	if( bind(sock,(struct sockaddr*)&addr,sizeof(struct sockaddr_in)) == -1 ) {
		error("[Server]: Could not bind socket!\n");
	}

	struct sockaddr_in clientSock;
	
	while(1) {
		struct sockaddr_in clientSock;
		int dataLen = 0;
		socklen_t clientLen = sizeof(clientSock);
		int received = recvfrom(sock,&dataLen,sizeof(int),0,(struct sockaddr*)&clientSock,&clientLen);
		
		if( received == -1 ) {
			error("[Server]: Client did not send the numbers.\n");
		}
		
		int port = ntohs(clientSock.sin_port);
		char *address = inet_ntoa(clientSock.sin_addr);
		printf("[Server]: Client connected: %s::%d\n",address,port);
		
		struct Request *r = (struct Request*)malloc(sizeof(struct Request));
		r->clientLen = clientLen;
		r->sock = sock;
		r->clientSocket = clientSock;
		r->dataLen = dataLen;

		pthread_t clientThread;
		pthread_create(&clientThread,NULL,handle_client,r);
	}

//	close(sock);

	return 0;
}
