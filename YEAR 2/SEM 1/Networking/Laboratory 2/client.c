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

int main(void) {
	int sock = socket(AF_INET,SOCK_STREAM,0);

	if( sock == -1) {
		error("Unable to create socket!");
	}
	// set-up server socket
	struct sockaddr_in server;
	memset(&server,0,sizeof(struct sockaddr_in));
	server.sin_family = AF_INET;
	server.sin_port = htons(PORT);
	server.sin_addr.s_addr = inet_addr("127.0.0.1");
	socklen_t serverLen = sizeof(struct sockaddr_in);

	// connect client to server
	int connected = connect(sock,(struct sockaddr*)&server,serverLen);

	if( connected == -1) {
		error("[Client]: Could not connect to server.\n");
	}

	printf("Connected to server.\n");

	int sent = 0;
	int received = 0;

	// prepare data to be sen
	uint16_t dataLen = 5;
	uint32_t data[] = {1,2,3,4,5};
	
	// send data length first
	uint16_t dataLenNet = htons(dataLen);
	sent = send(sock,&dataLenNet,sizeof(dataLenNet),0);
	
	if( sent == -1) {
		error("[Client]: Could not send data length.\n");
	}
	
	// send the actual data
	sent = send(sock,&data,dataLen * sizeof(uint32_t),0);

	if( sent == -1) {
		error("[Client]: Could not send data.\n");
	}

	uint32_t sum = 0;
	received = recv(sock,&sum,sizeof(sum),0);
	
	if( received == -1) {
		error("[Client]: Could not receive sum.\n");
	}

	printf("Got sum from server: %d\n",sum);

	return 0;
}
