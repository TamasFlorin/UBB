/*
	3. Write a program that finds the connected components of an undirected graph using a depth-first traversal of the graph.
*/
#include <iostream>
#include <fstream>
#include <vector>
#include <set>

#include "UndirectedGraph.h"

/**
* @brief depth first search traversal of the graph
* @param g undirected graph
* @param visited vector of visited nodes
* @param component current connected component
*/
void dfs(UndirectedGraph<int> &g, int source, std::vector<bool> &visited, std::set<int> &component)
{
	visited[source] = true;

	component.insert(source);

	for (auto it = g.OutNeighboursBegin(source); it != g.OutNeighboursEnd(source); it++)
	{
		if (!visited[*it])
		{
			dfs(g, *it, visited, component);
		}
	}

}
/**
* @brief get the connected components by calling DFS for each vertex
* @param g undirected graph
* @return vector of sets containing the connected components
*/
std::vector<std::set<int>> get_connected_components(UndirectedGraph<int> &g)
{
	std::vector<bool> visited(g.CountVertices(),false);
	std::vector<std::set<int>> components;

	for(int i = 0;i<g.CountVertices();i++)
	{ 
		// if the current vertex is not part of another component
		if (!visited[i])
		{
			// find the accessible vertices
			std::set<int> component;

			dfs(g, i, visited, component);

			// the accessible vertices form a component
			components.push_back(component);
		}
	}

	return components;
}

int pw2_3(void)
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
	
	std::vector<std::set<int>> components = get_connected_components(g);

	std::cout << "There is\\are " << components.size() << " component\\s."<< std::endl;

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