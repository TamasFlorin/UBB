#include "Common.h"

void print_menu() {
	printf("1.First n pairs of twin numbers.\n");
	printf("2.Longest decreasing contigous subsequence.\n");
	printf("x.Exit\n");
}

void ui_lds() {
	printf("n=");
	int n;
	scanf("%d", &n);

	// alloc memory for the result
	int *v = (int*)malloc(sizeof(int) *n);

	for (int i = 0; i < n; i++) {
		printf("v[%d]=", i);
		scanf("%d", &v[i]);
	}

	int start = 0, end = 0;
	lds(v,n,&start,&end);

	// no solution was found
	if (!end) {
		printf("No decreasing subsequence!\n");
		free(v);
		return;
	}

	printf("Found sequence with length %d:\n", end - start + 1);

	for (int i = start; i <= end; i++) {
		printf("%d ", v[i]);
	}

	free(v);

	printf("\n");
}

void ui_twin_primes() {
	int n;
	printf("Number of pairs:");
	scanf("%d", &n);

	int * result = (int*)malloc(2*n*sizeof(int));
	twin_primes(n, result);

	for (int i = 0; i < 2*n-1; i+=2) {
		printf("(%d,%d)\n", result[i],result[i+1]);
	}

	free(result);

	printf("\n");
}

void execute_command(char *command) {
	if (!strcmp(command, "1"))
		ui_twin_primes();

	else if (!strcmp(command, "2"))
		ui_lds();

	else if (!strcmp(command, "x"))
		exit(0xDEADBEEF);
	else 
		printf("Invalid command provided.\n");
}

void run() {
	
	print_menu();
	char command[COMMAND_LEN];

	while (true) {
		scanf("%s", command);
		execute_command(command);
	}
}