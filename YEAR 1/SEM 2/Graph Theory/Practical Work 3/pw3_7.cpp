/*
	7. Write a program that, given a graph with costs that has no negative cost cycles 
	and two vertices, finds a lowest cost walk between the given vertices. 
	The program shall use the Floyd-Warshall algorithm.
*/

#include <iostream>
#include <fstream>
#include <vector>

#include "DirectedGraphData.h"

void floyd_warshall(DirectedGraphData<int, int> &g, int source, int destination)
{
	const int infinity = std::numeric_limits<int>::max();
	std::vector<std::vector<int>> dist(g.CountVertices(), std::vector<int>(g.CountVertices(), infinity));
	std::vector<std::vector<int>> next(g.CountVertices(), std::vector<int>(g.CountVertices(), -1));

	// distance from a vertex to itself is 0
	for (int i = 0; i < g.CountVertices(); i++)
		dist[i][i] = 0;

	// set the weights for each edge
	for (int i = 0; i < g.CountVertices(); i++)
	{
		for (auto it = g.OutNeighboursBegin(i); it != g.OutNeighboursEnd(i); it++) {
			dist[i][*it] = g.GetData(i, *it);
			next[i][*it] = *it;
		}
	}

	for (int k = 0; k <g.CountVertices(); k++)
	{
		for (int i = 0; i<g.CountVertices(); i++)
			for (int j = 0; j < g.CountVertices(); j++) {
				if (dist[i][k] == infinity || dist[k][j] == infinity) continue;
				if (dist[i][j] > dist[i][k] + dist[k][j]) {
					dist[i][j] = dist[i][k] + dist[k][j];
					next[i][j] = next[i][k];
				}
			}
	}

	// in order to check if the given graph contains negative cycles
	// we can just search for negative values on the main diagonal
	for (int i = 0; i < g.CountVertices(); i++)
	{
		if (dist[i][i] < 0) {
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
	std::cout << "Found a walk of cost " << dist[source][destination] << ":" << std::endl;

	while (source != destination) {
		std::cout << source << "->";
		source = next[source][destination];
	}

	std::cout << destination << std::endl;
}

int pw3_7(void)
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

	floyd_warshall(g, 0, 6);

	std::cin.get();

	return 0;
}