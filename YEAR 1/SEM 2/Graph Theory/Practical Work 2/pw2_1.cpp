/*
	1. Write a program that, given a directed graph and two vertices, finds a lowest length path between them, by using a forward breadth-first search from the starting vertex.
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <queue>

#include "DirectedGraph.h"

/**
* @brief determine the lowest length path from source to destination
* @param g directed graph
* @param source the first node in the path
* @param destination the last node in the path
* @return a pair composed of the length of the path and a vector containing the prev vertices
*/
std::pair<int,std::vector<int>> lowest_length_path_forward(DirectedGraph<int> &g,int source,int destination)
{
	const int infinity = std::numeric_limits<int>::max();

	std::vector<int> length(g.CountVertices(),infinity);
	std::vector<int> prev(g.CountVertices(), -1);

	// the length of the path from source to itself is 0
	length[source] = 0;

	std::queue<int> q;

	// add the source vertex to the queue
	q.push(source);

	std::vector<bool> visited(g.CountVertices());

	visited[source] = true;

	while (!q.empty())
	{
		// get current vertex to process
		int vertex = q.front();

		// remove vertex
		q.pop();

		// process the neighbours of the current vertex
		for (auto neighbour = g.OutNeighboursBegin(vertex); neighbour != g.OutNeighboursEnd(vertex); neighbour++)
		{
			if (!visited[*neighbour])
			{
				// compute new length
				length[*neighbour] = length[vertex] + 1;

				// add it to the queue
				q.push(*neighbour);

				prev[*neighbour] = vertex;

				// set it as visited
				visited[*neighbour] = true;
			}
		}
	}

	return { length[destination],prev };
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

int pw2_1(void)
{
	std::ifstream in("g.txt");
	int n;
	in >> n;
	int m;
	in >> m;
	DirectedGraph<int> g(n);

	for (int i = 0; i < m; i++)
	{
		int src, dst;
		in >> src >> dst;
		g.AddEdge(src, dst);
	}

	in.close();

	int source = 0, destination = 6;

	auto res = lowest_length_path_forward(g, source, destination);

	if (res.second[destination] == -1) {
		std::cout << "No path from " << source << " to " << destination << " found!";
		return 1;
	}

	std::cout << "Found a path of length: "<<res.first <<std::endl;

	print_path_rec(res.second, source, destination);

	std::cin.get();

	return 0;
}