#pragma once

#include <map>
#include "DirectedGraph.h"

template<typename T,typename D>
class DirectedGraphData : public DirectedGraph<T>
{
	// represent the cost as a map of pairs and int
	std::map<std::pair<T, T>, D> data;
public:
	// custom constructor
	explicit DirectedGraphData(int n) : DirectedGraph<T>(n) {
	}

	explicit DirectedGraphData(const DirectedGraphData<T,D> &g) : DirectedGraph<T>(g) {
		data = g.data;
	}

	// Add edge and data
	void AddEdge(T x,T y,D d) {
		DirectedGraph<T>::AddEdge(x, y);
		data[{x, y}] = d;
	}

	// remove edge and data
	void RemoveEdge(T x, T y) {
		DirectedGraph<T>::RemoveEdge(x, y);
		data.erase({ x,y });
	}

	// set the data for a given edge
	void SetData(T x, T y,D d) {
		if (!IsValidVertex(x) || !IsValidVertex(y))
			throw GraphException("[SetData]: Invalid vertices provided!");

		data[{x, y}] = d;
	}

	// remove the data from the edge
	void RemoveData(T x, T y) {
		data.erase({ x,y });
	}

	// get the data from a given edge
	D GetData(T x, T y) {
		if (!IsValidVertex(x) || !IsValidVertex(y))
			throw GraphException("[GetData]: Invalid vertices provided!");

		return data[{x, y}];
	}
};
