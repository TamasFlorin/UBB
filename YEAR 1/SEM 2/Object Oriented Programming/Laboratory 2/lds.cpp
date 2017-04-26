#include "Common.h"

/*
* Function : lds
*---------------
*	Find the longest decreasing subsequence in a given array.
*
*	v(in) - array
*	n(in) - number of elements from the array
*	start(out) - will represent the starting of the lds
*   end(out) - will represent the ending of the lds
*/
void lds(int *v, int n,int *start,int *end) {
	int count = 1, max = 1;
	
	*start = *end = 0;
	int first = 0;

	for (int i = 1; i < n; i++) {
		if (v[i-1] > v[i]) 
			count++;
		else {
			count = 1;
			first = i;
		}
		if (count > max) {
			max = count;
			*end = i + 1;
			*start = first;
		}
	}
}
