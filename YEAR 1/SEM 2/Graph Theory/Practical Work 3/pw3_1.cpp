/*
	1. Write a program that, given a graph with positive costs and two vertices, 
	finds a lowest cost walk between the given vertices, using the Dijkstra algorithm. 
*/
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <functional>

#include <queue>

#include "DirectedGraphData.h"

/**
* @brief for a given source node find the shortest path between that node and the destination node
* @parem g directed graph with costs
* @param source the first node in the path
* @param destination the last node in the path
* @return a pair where the first item is the distance to from source to destination and the second item is the vector of previous nodes
*/
std::pair<uint32_t,std::vector<int>> dijkstra(DirectedGraphData<uint32_t, uint32_t> &g, uint32_t source, uint32_t destination)
{
	const uint32_t infinity = std::numeric_limits<uint32_t>::max();

	// distance
	std::vector<uint32_t> dist(g.CountVertices(), infinity);
	
	// used for optimization(if a node is already in the queue,it shouldn't be added)
	std::vector<bool> inQueue(g.CountVertices(), false);

	// beware this declaration
	std::priority_queue < std::pair<uint32_t, uint32_t>, std::vector<std::pair<uint32_t, uint32_t>>, std::greater<std::pair<uint32_t, uint32_t>>> pq;

	// distance from source to itself is 0
	dist[source] = 0;

	// push the source node using it's distance as the key
	pq.push({ dist[source],source });

	// source is now in the queue
	inQueue[source] = true;

	// map each accessible vertex to it's predecessor on a path from source to destination
	std::vector<int> prev(g.CountVertices(),-1);

	while (!pq.empty())
	{
		uint32_t from = pq.top().second;
		pq.pop();

		inQueue[from] = false;

		for (auto it = g.OutNeighboursBegin(from); it != g.OutNeighboursEnd(from); it++)
		{
			uint32_t to = *it;
			uint32_t cost = g.GetData(from, to);

			// relax
			if (dist[to] > dist[from] + cost)
			{
				// update distance
				dist[to] = dist[from] + cost;
				
				prev[to] = from;

				// we have reached the destination node
				if (to == destination)
					return { dist[to],prev };

				if (!inQueue[to])
				{
					inQueue[to] = true;
					pq.push({ dist[to],to });
				}
			}

		}
	}

	return { dist[destination],prev };
}

/**
* @brief recursive function to print the path represented on a vector of previous vertices
* @param prev vector containing the previous vertex for each vertex
* @param source the first node in the path
* @param destination the last node in the path
*/
void print_path_rec(const std::vector<int> &prev, int source, int destination)
{
	if (source == destination) {
		std::cout << source << " ";
		return;
	}
	print_path_rec(prev, source, prev[destination]);

	std::cout << destination << " ";
}

int main(void)
{
	std::ifstream in("dijkstra.txt");
	int n, m;
	in >> n >> m;

	DirectedGraphData<uint32_t, uint32_t> g(n);

	for (int i = 0; i < m; i++)
	{
		uint32_t from, to,cost;
		in >> from >> to >> cost;
		g.AddEdge(from, to, cost);
	}
	
	in.close();
	
	int source = 0, destination = 6;
	auto res = dijkstra(g, source, destination);

	if (res.second[destination] == -1) {
		std::cout << "No walk from " << source << " to " << destination << " found!" << std::endl;
		return 1;
	}

	std::cout << "Found a walk of cost: " << res.first << std::endl;

	print_path_rec(res.second, source, destination);

	std::cin.get();

	return 0;
}