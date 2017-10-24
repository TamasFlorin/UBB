/*
	4. Write a program that finds the connected components of an undirected graph using a breadth-first traversal of the graph.
*/
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <queue>

#include "UndirectedGraph.h"

/**
* @brief return a set with the accessible vertices starting from source
* @param g undidirected graph
* @param source starting node in the BFS traversal
* @return a set with the accessible vertices
*/
std::set<int> bfs(UndirectedGraph<int> &g, int source)
{
	std::set<int> component;
	std::queue<int> q;

	// add the first vertex to the queue
	q.push(source);

	// first vertex of the components is the source
	component.insert(source);

	while (!q.empty())
	{
		int vertex = q.front();

		q.pop();

		for (auto it = g.OutNeighboursBegin(vertex); it != g.OutNeighboursEnd(vertex); it++)
		{
			if (component.find(*it) == component.end())
			{
				q.push(*it);
				component.insert(*it);
			}
		}
	}

	return component;
}

/**
* @brief return a vector with all the connected components of the graph
* @param g undidirected graph
* @return a vector of sets containing the connected components
*/
std::vector<std::set<int>> get_connected_components_bfs(UndirectedGraph<int> &g)
{
	std::vector<bool> visited(g.CountVertices(), false);
	std::vector<std::set<int>> components;

	for (int i = 0; i<g.CountVertices(); i++)
	{
		// if current vertex is not part of another component
		if (!visited[i])
		{
			std::set<int> component = bfs(g, i);

			// set the vertices from the current component as visited(since they cannot be used anymore)
			for (auto v : component) visited[v] = true;

			// add current component
			components.push_back(component);
		}
	}

	return components;
}

int pw2_4(void)
{
	std::fstream in("comp.txt");
	int n, m;
	in >> n >> m;
	UndirectedGraph<int> g(n);

	for (int i = 0; i < m; i++) {
		int src, dst;
		in >> src >> dst;
		g.AddEdge(src, dst);
	}

	in.close();

	std::vector<std::set<int>> components = get_connected_components_bfs(g);

	std::cout << "There is\\are " << components.size() << " component\\s." << std::endl;

	for (auto comp : components)
	{
		for (auto v : comp)
		{
			std::cout << v << " ";
		}

		std::cout << std::endl;
	}

	std::cin.get();

	return 0;
}