/*
	5. Write a program that, given an undirected connected graph, constructs a minumal spanning tree using the Kruskal's algorithm.
*/
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <algorithm>

#include "UndirectedGraphData.h"

template<typename T>
class DisjointSet
{
	std::map<T, T> parent;
public:
	void make_set(T x) {
		parent[x] = x;
	}

	T find(T x)
	{
		if (parent[x] == x) {
			return x;
		}

		return parent[x] = find(parent[x]);
	}

	void union_set(T x, T y) {
		parent[find(x)] = find(y);
	}
};

std::vector<std::pair<std::pair<int,int>,int>> Kruskal(UndirectedGraphData<int,int> &g)
{
	DisjointSet<int> dSet;
	
	std::vector<std::pair<std::pair<int, int>, int>> sortedEdges;

	// create a vector containing all the edges and their cost
	for (int i = 0; i < g.CountVertices(); i++) {
		for (auto it = g.OutNeighboursBegin(i); it != g.OutNeighboursEnd(i); it++) {
			sortedEdges.push_back({ {i,*it},g.GetData(i,*it) });
		}
	}

	// sort the edges by cost
	std::sort(sortedEdges.begin(), sortedEdges.end(), [](auto e1, auto e2) {return e1.second < e2.second; });

	// make the empty sets
	for (int i = 0; i < g.CountVertices(); i++) {
		dSet.make_set(i);
	}
	
	std::vector<std::pair<std::pair<int, int>, int>> edges;
	for (auto edge : sortedEdges) {
		// if they are part of the same set,ignore them
		if (dSet.find(edge.first.first) == dSet.find(edge.first.second)) {
			continue;
		}

		// make them part of the same set
		dSet.union_set(edge.first.first, edge.first.second);

		// this edge is used in the MST
		edges.push_back({ { edge.first.first,edge.first.second }, edge.second });
	}
	
	return edges;
}

int pw4_5(void)
{
	std::fstream in("kruskal.txt");
	int n, m;
	in >> n >> m;
	UndirectedGraphData<int,int> g(n);

	for (int i = 0; i < m; i++) {
		int src, dst, cost;
		in >> src >> dst >> cost;
		g.AddEdge(src, dst,cost);
	}

	in.close();

	auto edges = Kruskal(g);

	for (auto edge : edges) {
		std::cout << edge.first.first << "->" << edge.first.second << " cost:" << edge.second << std::endl;
	}

	std::cin.get();

	return 0;
}