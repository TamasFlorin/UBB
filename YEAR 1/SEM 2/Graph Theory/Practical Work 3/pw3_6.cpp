/*
	6. Write a program that, given a graph with costs and two vertices, finds a lowest cost walk between 
	the given vertices, or prints a message if there are negative cost cycles in the graph. 
	The program shall use the matrix multiplication algorithm.
*/
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <stack>
#include "DirectedGraphData.h"
#include <algorithm>

typedef std::vector<std::vector<int>> matrix_t;

void matrix_multiplication(matrix_t &A, matrix_t &B, matrix_t &C,std::vector<std::vector<int>> &next)
{
	const int infinity = std::numeric_limits<int>::max();

	for (int i = 0; i < A.size(); i++) {
		for (int j = 0; j < B.size(); j++) {
			C[i][j] = infinity;
			for (int k = 0; k < C[j].size(); k++) {
				if (A[i][k] == infinity || B[k][j]==infinity) continue;
				//C[i][j]= std::min(C[i][j], A[i][k] + B[k][j]);
				if (C[i][j] > A[i][k] + B[k][j]) {
					C[i][j] = A[i][k] + B[k][j];
					next[i][j] = next[i][k];
				}
			}
		}
	}
}

void min_dist(DirectedGraphData<int, int> &g, int source, int destination)
{
	const int infinity = std::numeric_limits<int>::max();
	matrix_t D(g.CountVertices(),std::vector<int>(g.CountVertices(),infinity));

	matrix_t next(g.CountVertices(), std::vector<int>(g.CountVertices(), -1));

	// distance from a vertex to itself is 0
	for (int i = 0; i < g.CountVertices(); i++) {
		D[i][i] = 0;
	}

	// add the weights for each vertex
	for (int i = 0; i < g.CountVertices(); i++) {
		for (auto it = g.OutNeighboursBegin(i); it != g.OutNeighboursEnd(i); it++) {
			int cost = g.GetData(i, *it);
			D[i][*it] = cost;
			next[i][*it] = *it;
		}
	}

	matrix_t A = D;
	matrix_t C = D;

	for (int i = 2; i < g.CountVertices(); i++) {
		matrix_multiplication(A, D, C,next);
		A = C;
	}

	// check for cycle
	for (int i = 0; i < g.CountVertices(); i++)
	{
		if (C[i][i] < 0) {
			std::cout << "Graph contains negative cycles!" << std::endl;
			return;
		}
	}

	// check if there is a walk from source to destination
	if (next[source][destination] == -1) {
		std::cout << "No walk from " << source << " to " << destination << "!" << std::endl;
		return;
	}

	// if there is,print it
	std::cout << "Found a walk of cost " << C[source][destination] << ":" << std::endl;

	while (source != destination) {
		std::cout << source << "->";
		source = next[source][destination];
	}

	std::cout << destination << std::endl;
}

int pw3_6(void)
{
	std::ifstream in("floyd_warshall.txt");
	int n, m;
	in >> n >> m;

	DirectedGraphData<int, int> g(n);

	for (int i = 0; i < m; i++)
	{
		int from, to, cost;
		in >> from >> to >> cost;
		g.AddEdge(from, to, cost);
	}

	in.close();

	min_dist(g, 0, 3);

	std::cin.get();

	return 0;
}