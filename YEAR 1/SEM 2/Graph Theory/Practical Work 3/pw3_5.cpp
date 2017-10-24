/*
	5. Write a program that, given a graph with costs and two vertices, finds a lowest cost walk between 
	the given vertices, or prints a message if there are negative cost cycles accessible from the starting vertex.
	The program will use the Ford's algorithm.
*/
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <stack>
#include "DirectedGraphData.h"

void bellman_ford(DirectedGraphData<int,int> &g,int source,int destination)
{
	const int infinity = std::numeric_limits<int>::max();
	const int invalidPred = -1;

	std::vector<int> dist(g.CountVertices(),infinity);

	dist[source] = 0;

	std::vector<int> predecessor(g.CountVertices(),invalidPred);

	// max V-1 relaxations
	for (int i = 0; i < g.CountVertices() - 1; i++)
	{
		for (int v = 0; v < g.CountVertices(); v++)
		{
			int from = v;
			for (auto it = g.OutNeighboursBegin(v); it != g.OutNeighboursEnd(v); it++)
			{
				int to = *it;
				int cost = g.GetData(from, to);

				if (dist[to] > dist[from] + cost)
				{
					dist[to] = dist[from] + cost;
					predecessor[to] = from;
				}
			}
		}
	}

	// check for negative cycle
	for (int v = 0; v < g.CountVertices(); v++)
	{
		int from = v;
		for (auto it = g.OutNeighboursBegin(v); it != g.OutNeighboursEnd(v); it++)
		{
			int to = *it;
			int cost = g.GetData(from, to);

			if (dist[to] > dist[from] + cost)
			{
				std::cout << "Graph contains negative cycle!" << std::endl;
				return;
			}
		}
	}

	if (predecessor[destination] == -1) {
		std::cout << "No walk from " << source << " to " << destination << "!"<<std::endl;
		return;
	}

	
	// AICI INCEPE AFISAREA
	std::cout << "Found walk of cost: " << dist[destination] << "." << std::endl;

	std::stack<int> walk;
	int current = destination;
	while (source != current) {
		walk.push(current);
		current = predecessor[current];
	}
	std::cout << source << "->";
	while (!walk.empty()) {
		if(walk.size()>1) std::cout << walk.top() << "->";
		else std::cout << walk.top() << std::endl;

		walk.pop();
	}

}

int pw3_5(void)
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


	bellman_ford(g, 0, 6);

	//std::cout << dijkstra_backward(g, 0, 6) << std::endl;

	std::cin.get();

	return 0;
}