/*
	1B. Write a program that finds the strongly-connected components of a directed graph in O(n+m) (n=no. of vertices, m=no. of arcs)
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <stack>
#include <algorithm>

#include "DirectedGraph.h"

void dfs_time(DirectedGraph<int> &g, int source, std::vector<bool> &visited, std::stack<int> &nodes)
{
	visited[source] = true;

	for (auto it = g.OutNeighboursBegin(source); it != g.OutNeighboursEnd(source); it++)
	{
		if (!visited[*it])
		{
			dfs_time(g, *it, visited, nodes);
		}
	}


	// finished exploring all it's neighbours,add it to the stack
	nodes.push(source);
}

void dfs(DirectedGraph<int> &g, int source, std::vector<bool> &visited, std::set<int> &component)
{
	visited[source] = true;
	component.insert(source);

	for (auto it = g.InNeighboursBegin(source); it != g.InNeighboursEnd(source); it++)
	{
		if (!visited[*it])
		{
			dfs(g, *it, visited, component);
		}
	}
}

std::vector<std::set<int>> get_strongly_connected_comp(DirectedGraph<int> &g)
{
	std::vector<bool> visited(g.CountVertices(),false);
	std::stack<int> nodes;

	for(int i = 0; i < g.CountVertices();i++)
		if (!visited[i])
			dfs_time(g, i, visited, nodes);

	std::fill(visited.begin(), visited.end(), false);

	std::vector<std::set<int>> components;
	
	while (!nodes.empty())
	{
		int node = nodes.top();

		nodes.pop();

		if (!visited[node])
		{
			std::set<int> component;
			dfs(g, node, visited, component);
			components.push_back(component);
		}
	}

	return components;
}

int pw2_1B(void)
{
	std::ifstream in("s_comp.txt");
	int n, m;
	in >> n >> m;

	DirectedGraph<int> g(n);

	for (int i = 0; i < m; i++)
	{
		int src, dst;
		in >> src >> dst;
		g.AddEdge(src, dst);
	}

	in.close();

	auto components = get_strongly_connected_comp(g);

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