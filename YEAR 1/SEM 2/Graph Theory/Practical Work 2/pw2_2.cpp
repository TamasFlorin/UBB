#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <stack>

#include "DirectedGraph.h"
/**
* @brief determine the lowest length path from source to destination using a backwards BFS
* @param g directed graph
* @param source the first node in the path
* @param destination the last node in the path
* @return a pair composed of the length of the path and a vector containing the prev vertices
*/
std::pair<int,std::vector<int>> lowest_length_path_backward(DirectedGraph<int> &g, int source, int destination)
{
	const int infinity = std::numeric_limits<int>::max();

	std::vector<int> length(g.CountVertices(), infinity);

	// the length of the path from destination to itself is 0
	length[destination] = 0;

	std::queue<int> q;

	// add the source vertex to the queue
	q.push(destination);

	std::vector<bool> visited(g.CountVertices());

	visited[destination] = true;

	std::vector<int> prev(g.CountVertices(),-1);
	std::vector<int> next(g.CountVertices(), -1);
	while (!q.empty())
	{
		// get current vertex to process
		int vertex = q.front();

		// remove vertex
		q.pop();

		// process the neighbours of the current vertex
		for (auto neighbour = g.InNeighboursBegin(vertex); neighbour != g.InNeighboursEnd(vertex); neighbour++)
		{
			if (!visited[*neighbour])
			{
				length[*neighbour] = length[vertex] + 1;
				q.push(*neighbour);
				
				next[*neighbour] = vertex;

				visited[*neighbour] = true;
			}
		}
	}

	return { length[source], next };
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

int pw2_2(void)
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

	auto res = lowest_length_path_backward(g, source, destination);

	if (res.second[source] == -1) {
		std::cout << "No path from " << source << " to " << destination << " found!";
		return 1;
	}

	std::cout << "Found a path of length: " << res.first << std::endl;

	print_path_rec(res.second, source, destination);

	std::cin.get();

	return 0;
}