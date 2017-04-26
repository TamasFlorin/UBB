#pragma once

#include "DirectedGraph.h"

template<typename T>
class UndirectedGraph : public DirectedGraph<T>
{
public:
	UndirectedGraph() : DirectedGraph<T>() {}

	explicit UndirectedGraph(int n) : DirectedGraph<T>(n) {}

	explicit UndirectedGraph(const UndirectedGraph<T> &g) : DirectedGraph<T>(g){}

	void AddEdge(T x, T y)
	{
		DirectedGraph<T>::AddEdge(x, y);
		DirectedGraph<T>::AddEdge(y, x);
	}

	void RemoveRedge(T x, T y)
	{
		DirectedGraph<T>::RemoveEdge(x, y);
		DirectedGraph<T>::RemoveEdge(x, y);
	}
};
