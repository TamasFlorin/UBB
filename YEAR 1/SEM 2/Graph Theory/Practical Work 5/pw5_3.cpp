/*
	3. Given an undirected graph, find a vertex coloring with minimum number of colors.
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>

#include "UndirectedGraph.h"

void vertex_coloring(UndirectedGraph<int> &g)
{
	// resulting map <vertex,color>
	std::map<int, int> result;

	// iterate over all vertices
	for (int i = 0; i < g.CountVertices(); i++)
	{
		// set to retain assigned colors
		std::set<int> assigned;

		// try to assign a color to current vertex
		for (auto it = g.OutNeighboursBegin(i); it != g.OutNeighboursEnd(i); it++) {
			if (result[*it])
				assigned.insert(result[*it]); // assign current unused color
		}

		// check for the first available color
		int color = 1;
		for (auto c : assigned) {
			if (c != color) break;
			color++;
		}

		result[i] = color;
	}

	for (int i = 0; i < g.CountVertices(); i++)
		std::cout << "Color assigned to vertex " << i << " is " << result[i] << std::endl;
}

int main(void)
{
	std::fstream in("color.txt");

	int n, m;
	in >> n >> m;

	UndirectedGraph<int> g(n);
	
	for (int i = 0; i < m; i++)
	{
		int src, dst;
		in >> src >> dst;
		g.AddEdge(src, dst);
	}

	in.close();
	vertex_coloring(g);

	std::cin.get();

	return 0;
}