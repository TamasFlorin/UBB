/*
	6. Write a program that, given an undirected connected graph, constructs a minumal spanning tree using the Prim's algorithm.
*/
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <algorithm>
#include <queue>
#include <functional>

#include "UndirectedGraphData.h"

// Find the minimum edge that can be made using the visited vertices
std::pair<int,int> get_min_edge(UndirectedGraphData<int, int> &g, std::set<int> &visited)
{
	int min = std::numeric_limits<int>::max();
	int minNode = *visited.begin();
	int currNode = *visited.begin();

	for (auto node : visited) {
		for (auto it = g.OutNeighboursBegin(node); it != g.OutNeighboursEnd(node); it++) {

			// current node is already in the MST,ignore it
			if (visited.find(*it) != visited.end()) continue;

			int cost = g.GetData(node, *it);

			// compute the new minimum cost and save the edge information
			if (cost < min) {
				min = cost;
				minNode = *it;
				currNode = node;
			}
		}
	}

	// add the used vertex to the visited set
	visited.insert(minNode);

	return { currNode,minNode };
}

// no priority queue
std::set<std::pair<std::pair<int, int>, int>> prim_simple(UndirectedGraphData<int, int> &g)
{
	// visited vertices
	std::set<int> visited;

	// we will start from vertex 0
	visited.insert(0);

	// edges that are part of the MST
	std::set<std::pair<std::pair<int, int>, int>> edges;

	// we have to find V-1 edges
	for (int i = 0; i < g.CountVertices() - 1; i++) {
		std::pair<int,int> edge = get_min_edge(g, visited);
		
		edges.insert({ edge,g.GetData(edge.first,edge.second) });
	}

	return edges;
}

// Prim's algorithm using a priority queue
// will return the list of parent vertices
std::vector<int> prim_priority_queue(UndirectedGraphData<int, int> &g)
{
	const int infinity = std::numeric_limits<int>::max();

	std::priority_queue <std::pair<int, int>, std::vector<std::pair<int, int> >, std::greater<std::pair<int,int>>> pq;

	std::vector<int> dist(g.CountVertices(), infinity);
	std::vector<int> parent(g.CountVertices(), -1);

	std::set<int> visited;

	// start from vertex 0
	// the distance from vertex 0 to itself is 0
	dist[0] = 0;
	pq.push({ dist[0],0 });

	while (!pq.empty()) 
	{
		int u = pq.top().second;
		pq.pop();

		// add current vertex to MST
		visited.insert(u);

		for (auto it = g.OutNeighboursBegin(u); it != g.OutNeighboursEnd(u); it++)
		{
			int v = *it;
			int cost = g.GetData(u,v);

			if (visited.find(v) != visited.end()) continue;

			// update the cost for the current vertex
			if (cost < dist[v]) {
				dist[v] = cost;
				pq.push({ dist[v],v });
				parent[v] = u;
			}
		}
	}

	return parent;
}

int pw4_6(void)
{
	std::fstream in("kruskal.txt");
	int n, m;
	in >> n >> m;
	UndirectedGraphData<int, int> g(n);

	for (int i = 0; i < m; i++) {
		int src, dst, cost;
		in >> src >> dst >> cost;
		g.AddEdge(src, dst, cost);
	}

	in.close();

	// using simple Prim's algorithm
	auto edges = prim_simple(g);

	std::cout << "Simple Prime:" << std::endl;
	for (auto edge : edges) {
		std::cout << edge.first.first << "->" << edge.first.second << " cost:" << edge.second << std::endl;
	}

	std::cout << "Prime with priority queue:" << std::endl;

	auto parent = prim_priority_queue(g);

	for (int i = 1; i < g.CountVertices(); i++)
		std::cout << parent[i] << "->" << i << " cost:"<<g.GetData(parent[i],i) << std::endl;

	std::cin.get();

	return 0;
}