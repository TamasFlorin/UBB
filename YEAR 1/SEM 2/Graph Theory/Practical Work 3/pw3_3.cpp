/*
  3. Write a program that, given a graph with costs and two vertices, finds a lowest cost walk between the given vertices, or prints a message 
  if there are negative cost cycles accessible from the starting vertex. The program will use a matrix defined as d[x,k]=the cost of the lowest 
  cost walk from s to x and of length at most k, where s is the starting vertex.
*/

#include <iostream>
#include <fstream>
#include <vector>

#include "DirectedGraphData.h"

std::vector<int> min_cost_dynamic(DirectedGraphData<int,int> & g, int start_node, int max_levels)
{
	const int infinity = std::numeric_limits<int>::max();

	max_levels++; //to accomodate for 0 
	std::vector< std::vector< int > > dist(max_levels,std::vector<int>(g.CountVertices(),0)); //min dist[k][x] = dist at lvl k from s to x

	for (int x = 0; x < g.CountVertices(); x++)
	{
		dist[0][x] = infinity;
	}

	dist[0][start_node] = 0;

	for (int k = 1; k < max_levels; k++)
		for (int x = 0; x < g.CountVertices(); x++)
		{
			dist[k][x] = dist[k - 1][x];
			for (auto it = g.OutNeighboursBegin(x);it!=g.OutNeighboursEnd(x);it++)
			{
				if (dist[k][x] > dist[k - 1][*it] + g.GetData(*it, x))
					dist[k][x] = dist[k - 1][*it] + g.GetData(*it, x);
			}
		}

	return dist[max_levels - 1];
}

int pw3_3(void)
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

	auto res = min_cost_dynamic(g, 0, 4);

	std::cin.get();

	return 0;
}