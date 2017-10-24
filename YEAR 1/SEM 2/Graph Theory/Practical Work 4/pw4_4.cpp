/*
	4. Write a program that, given a graph with costs, does the following:
		-verify if the corresponding graph is a DAG and performs a topological sorting of 
		the activities using the algorithm based on predecessor counters;
		-if it is a DAG, finds a highest cost path between two given vertices, in O(m+n).
*/
#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <stack>

#include "DirectedGraphData.h"

enum VertexState
{
	E_UNEXPLORED = 0,
	E_EXPLORING = 1,
	E_EXPLORED = 2
};

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

std::set<int> topo_sort(DirectedGraphData<int, int> &g)
{
	std::vector<int> degree(g.CountVertices(),0);
	std::set<int> nodes;

	std::queue<int> q;

	for (int i = 0; i < g.CountVertices(); i++)
	{
		degree[i] = g.GetInDegree(i);

		if (degree[i] == 0)
			q.push(i);
	}

	while (!q.empty())
	{
		int node = q.front();

		q.pop();

		nodes.insert(node);

		for (auto it = g.OutNeighboursBegin(node); it != g.OutNeighboursEnd(node); it++) {
			if (--degree[*it] == 0) {
				q.push(*it);
			}
		}
	}

	return nodes;
}

std::pair<int,std::vector<int>> max_dist_DAG(DirectedGraphData<int, int> &g, int source, int destination)
{
	std::set<int> nodes = topo_sort(g);

	const int infinity = std::numeric_limits<int>::min();

	std::vector<int> dist(nodes.size(), infinity);

	std::vector<int> prev(g.CountVertices(), -1);

	dist[source] = 0;

	for (auto node : nodes) {
		for (auto it = g.OutNeighboursBegin(node); it != g.OutNeighboursEnd(node); it++) {
			int cost = g.GetData(node, *it);

			// max distance
			if (dist[*it] < dist[node] + cost) {
				dist[*it] = dist[node] + cost;
				prev[*it] = node;
			}
		}
	}

	return { dist[destination] , prev };
}


void print_path_rec(const std::vector<int> &prev, int source, int destination)
{
	if (source == destination) {
		std::cout << source << " ";
		return;
	}
	print_path_rec(prev, source, prev[destination]);

	std::cout << destination << " ";
}

int pw4(void)
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

	int source = 0, destination = 3;

	auto res = max_dist_DAG(g, source, destination);

	if (res.second[destination] == -1) {
		std::cout << "No path from " << source << " to " << destination << " found!" << std::endl;
		return 1;
	}

	std::cout << "Found a path of cost: " << res.first << std::endl;

	print_path_rec(res.second, source, destination);

	std::cin.get();

	return 0;
}