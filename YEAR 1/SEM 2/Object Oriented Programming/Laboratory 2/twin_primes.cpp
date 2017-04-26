#include "Common.h"

#define MAX_PRIMES 10000000

/*
* Function : sieve
*---------------
*	Set the first n positions of a vector to 1 if i is prime and 0 otherwise. 
*	
*	n(in) - maximum number
*   out(out) - the resulting array
*/
void sieve(int n, int *out) {
	memset(out, 1, sizeof(out));

	for (int i = 2; i*i<= n; i++) {
		if (out[i]) {
			for (int j = i * 2; j <= n; j += i) {
				out[j] = 0;
			}
		}
	}
}

/*
* Function : generate_primes
*---------------
*	Generate an array of prime numbers.
*
*	n(in) - upper bound
*   out(out) - the resulting array
*   size(out) - the size of the resulting array
*/
void generate_primes(int n, int *out, int*size) {
	// alloc memory for the sieve
	int *c = (int*)malloc(sizeof(int) *(n + 1));

	sieve(n, c);

	int count = 0;

	for (int i = 0; i <= n; i++) {
		if (c[i]) {
			out[count++] = i;
		}
	}

	*size = count;

	// free the memory allocated for the sieve
	free(c);
}

/*
* Function : twin_primes
*---------------
*	Generate the first n twin prime pairs.
*
*	n(in) - number of pairs to generate,
*   out(out) - array to store the pairs
*/
void twin_primes(int n,int *out) {

	// alloc memory for the prime numbers
	int *primes = (int*)malloc(sizeof(int) * (MAX_PRIMES + 1));

	// size of the 'primes' array
	int size = 0;

	// generate the prime numbers
	generate_primes(MAX_PRIMES + 1, primes, &size);

	int count = 0; // current number of pairs
	int current = 0; // current position in the array

	for (int i = 1; i < size; i++) {
		if (primes[i] - primes[i - 1] == 2) {
			out[current++] = primes[i - 1];
			out[current++] = primes[i];
			count++;
		}

		if (count >= n) {
			break;
		}
	}

	// free the allocated memory
	free(primes);
}
