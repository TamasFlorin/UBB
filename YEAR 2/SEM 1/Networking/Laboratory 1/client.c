#include <stdio.h>
#include <string.h>
#include <netinet/ip.h>
#include <arpa/inet.h>
#include <stdlib.h>
#include <unistd.h>

#define PORT 1337

void error(char *msg) {
	printf("%s\n",msg);
	exit(0xDEAD);
}

int main(void) {
	// create socket
	int sock = socket(AF_INET,SOCK_DGRAM,0);
	
	if( sock == -1) {
		error("Could not create socket!\n");
	}
	
	struct sockaddr_in addr;
	addr.sin_family = AF_INET;
	addr.sin_port = htons(PORT);
	addr.sin_addr.s_addr = inet_addr("127.0.0.1");
	
	int data[] = {1,2,3,4,5};
	int dataLen = sizeof(data) / sizeof(int);

	socklen_t sockLen = sizeof(struct sockaddr_in);

	dataLen = htons(dataLen);
	int sentLen = sendto(sock,&dataLen,sizeof(int),0,(struct sockaddr*)&addr,sizeof(struct sockaddr_in));
	
	int port = 0;
	int recvLen = recvfrom(sock,&port,sizeof(int),0,(struct sockaddr*)&addr,&sockLen);
	
	if( recvLen == -1) {
		error("Port not received!");
	}

	addr.sin_port = port;

	for(int i = 0; i < sizeof(data) / sizeof(int); i++) {
		data[i] = htons(data[i]);
	}

	int sent = sendto(sock,data,sizeof(data),0,(struct sockaddr*)&addr,sizeof(struct sockaddr_in));
	
	int sum = 0;

	int received = recvfrom(sock,&sum,sizeof(sum),0,(struct sockaddr*)&addr,&sockLen);

	if( received == -1) {
		perror("[Client]: Server did not send sum.\n");
	}

	sum = ntohs(sum);
	
	printf("[Client]: Got sum = %d\n",sum);

	close(sock);

	return 0;
}

