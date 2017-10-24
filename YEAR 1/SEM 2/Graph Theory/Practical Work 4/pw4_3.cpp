/*
	3. Write a program that, given a graph with costs, does the following:
		-verify if the corresponding graph is a DAG and performs a topological sorting of the activities 
		using the algorithm based on depth-first traversal (Tarjan's algorithm);
		-if it is a DAG, finds a highest cost path between two given vertices, in O(m+n).
*/
#include <iostream>
#include <fstream>
#include <vector>
#include <stack>

#include "DirectedGraphData.h"

enum VertexState
{
	E_UNEXPLORED = 0,
	E_EXPLORING = 1,
	E_EXPLORED = 2
};

// THIS IS ACTUALLY FOR DIRECTED GRAPH
void dfs_directed(DirectedGraph<int> &g, int source, std::vector<VertexState> &states, bool &hasCycle)
{
	states[source] = E_EXPLORING;

	for (auto it = g.OutNeighboursBegin(source); it != g.OutNeighboursEnd(source); it++) {
		if (states[*it] == E_UNEXPLORED) {
			dfs_directed(g, *it, states, hasCycle);
		}
		else if (states[*it] == E_EXPLORING) {
			hasCycle = true;
		}
	}

	states[source] = E_EXPLORED;
}

bool has_cycle_directed(DirectedGraphData<int, int> &g)
{
	bool hasCycle = false;
	std::vector<VertexState> states(g.CountVertices(), E_UNEXPLORED);

	for (int i = 0; i < g.CountVertices(); i++) {
		dfs_directed(g, i, states, hasCycle);
	}

	return hasCycle;
}

void topo_sort(DirectedGraphData<int, int> &g, int source, std::vector<bool> &visited,std::stack<int> &nodes)
{
	visited[source] = true;
	for (auto it = g.OutNeighboursBegin(source); it != g.OutNeighboursEnd(source); it++) {
		if (!visited[*it]) {
			topo_sort(g, *it, visited, nodes);
		}
	}

	nodes.push(source);
}

int max_dist_DAG(DirectedGraphData<int,int> &g,int source,int destination)
{
	std::stack<int> nodes;
	std::vector<bool> visited(g.CountVertices(),false);
	
	// topological sort of the vertices
	for (int i = 0; i < g.CountVertices(); i++) {
		if (!visited[i]) {
			topo_sort(g, i, visited, nodes);
		}
	}

	const int infinity = std::numeric_limits<int>::min();

	std::vector<int> dist(nodes.size(), infinity);

	dist[source] = 0;

	while (!nodes.empty())
	{
		int from = nodes.top();
		nodes.pop();

		for (auto it = g.OutNeighboursBegin(from); it != g.OutNeighboursEnd(from); it++) {
			int cost = g.GetData(from, *it);

			// max distance
			if (dist[*it] < dist[from] + cost) {
				dist[*it] = dist[from] + cost;
			}
		}
	}

	return dist[destination];
}

int main(void)
{
	std::ifstream in("dag.txt");
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

	if (has_cycle_directed(g)) {
		std::cout << "The given graph is not a DAG!" << std::endl;
		return 0;
	}

	std::cout<<max_dist_DAG(g, 0, 3);

	std::cin.get();

	return 0;
}