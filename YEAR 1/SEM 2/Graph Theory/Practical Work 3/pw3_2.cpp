/* 
	2. Write a program that, given a graph with positive costs and two vertices, finds a lowest cost walk between the given vertices, 
	using a "backwards" Dijkstra algorithm (Dijkstra algorithm that searches backwards, from the ending vertex).
*/
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <functional>

#include <queue>

#include "DirectedGraphData.h"

std::pair<uint32_t, std::vector<int>> dijkstra_backward(DirectedGraphData<uint32_t, uint32_t> &g, uint32_t source, uint32_t destination)
{
	const uint32_t infinity = std::numeric_limits<uint32_t>::max();

	// distance
	std::vector<uint32_t> dist(g.CountVertices(), infinity);

	// seen vertices
	std::vector<bool> inQueue(g.CountVertices(), false);

	// beware this declaration
	std::priority_queue < std::pair<uint32_t, uint32_t>, std::vector<std::pair<uint32_t, uint32_t>>, std::greater<std::pair<uint32_t, uint32_t>>> pq;

	dist[destination] = 0;
	pq.push({ dist[destination],destination });

	inQueue[destination] = true;

	std::vector<int> next(g.CountVertices(), -1);

	while (!pq.empty())
	{
		uint32_t from = pq.top().second;
		pq.pop();

		inQueue[from] = false;

		for (auto it = g.InNeighboursBegin(from); it != g.InNeighboursEnd(from); it++)
		{
			uint32_t to = *it;
			uint32_t cost = g.GetData(to, from);

			if (dist[to] > dist[from] + cost)
			{
				dist[to] = dist[from] + cost;
				next[to] = from;

				if (to == destination)
					return { dist[to],next };

				if (!inQueue[to])
				{
					inQueue[to] = true;
					pq.push({ dist[to],to });
				}
			}

		}
	}

	return { dist[source],next };
}

/**
* @brief recursive function to print the path represented on a vector of next vertices
* @param next vector containing the next vertex for each vertex
* @param source the first node in the path
* @param destination the last node in the path
*/
void print_path_rec(const std::vector<int> &next, int source, int destination)
{
	if (source == destination) {
		std::cout << source << " ";
		return;
	}
	std::cout << source << " ";

	print_path_rec(next, next[source], destination);
}

int main(void)
{
	std::ifstream in("dijkstra.txt");
	int n, m;
	in >> n >> m;

	DirectedGraphData<uint32_t, uint32_t> g(n);

	for (int i = 0; i < m; i++)
	{
		uint32_t from, to, cost;
		in >> from >> to >> cost;
		g.AddEdge(from, to, cost);
	}

	in.close();

	int source = 0, destination = 6;

	auto res = dijkstra_backward(g, source, destination);

	if (res.second[source] == -1) {
		std::cout << "No walk from " << source << " to " << destination << " found!" << std::endl;
		return 1;
	}

	std::cout << "Found a walk of cost " << res.first << std::endl;

	print_path_rec(res.second, source, destination);

	std::cin.get();

	return 0;
}