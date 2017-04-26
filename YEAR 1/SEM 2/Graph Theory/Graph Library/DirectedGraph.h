#pragma once

#include <map>
#include <set>
#include "IGraph.h"
#include "GraphException.h"

template <typename T>
class DirectedGraph : public IGraph<T> {
	std::map<T, std::set<T>> outNeighbours;
	std::map<T, std::set<T>> inNeighbours;
	std::set<T> vertices;

protected:
	// check if a givn vertex is valid
	bool IsValidVertex(T x) const {
		return vertices.find(x) != vertices.end();
	}

public:
	// custom constructor to allow initializaton of vertices
	explicit DirectedGraph(int n) {
		for (int i = 0; i < n; i++)
			vertices.insert(i);
	}

	explicit DirectedGraph(const DirectedGraph<T> & g) {
		outNeighbours = g.outNeighbours;
		inNeighbours = g.inNeighbours;
		vertices = g.vertices;
	}

	// default constructor
	DirectedGraph() {}

	// Add an edge between vertices x and y
	void AddEdge(T x, T y) {
		if (!IsValidVertex(x) || !IsValidVertex(y))
			throw GraphException("[AddEdge]: Invalid vertices provided!");

		outNeighbours[x].insert(y);
		inNeighbours[y].insert(x);
	}

	// Add a new vertex
	void AddVertex(T x) {
		vertices.insert(x);
	}

	// return an iterator to the begining of the vertices set
	typename std::set<T>::iterator VerticesBegin() {
		return vertices.begin();
	}

	// return a pointer to the end of the vertices set
	 auto VerticesEnd() {
		return vertices.end();
	}

	// return the number of vertices
	int CountVertices() const {
		return vertices.size();
	}

	// check if two vertices form an edge
	bool IsEdge(T x, T y) {
		if (!IsValidVertex(x) || !IsValidVertex(y))
			throw GraphException("[IsEdge]: Invalid vertices provided!");

		return outNeighbours[x].find(y) != outNeighbours[x].end();
	}

	// remove the edge between vertices x and y
	void RemoveEdge(T x, T y) {
		if (!IsValidVertex(x) || !IsValidVertex(y))
			throw GraphException("[RemoveEdge]: Invalid vertices provided!");

		outNeighbours[x].erase(y);
	}

	// in degree 
	int GetInDegree(T x) {
		if(!IsValidVertex(x))
			throw GraphException("[GetInDegree]: Invalid vertex provided!");

		return inNeighbours[x].size();
	}

	// out degree
	int GetOutDegree(T x) {
		if(!IsValidVertex(x))
			throw GraphException("[GetOutDegree]: Invalid vertex provided!");

		return outNeighbours[x].size();
	}

	auto OutNeighboursBegin(T x) 
	{
		if (!IsValidVertex(x))
			throw GraphException("[OutNeighboursBegin]: Invalid vertex provided!");

		return outNeighbours[x].begin();
	}

	auto OutNeighboursEnd(T x) {
		if (!IsValidVertex(x))
			throw GraphException("[OutNeighboursEnd]: Invalid vertex provided!");

		return outNeighbours[x].end();
	}

	auto InNeighboursBegin(T x) {
		if (!IsValidVertex(x))
			throw GraphException("[InNeighboursBegin]: Invalid vertex provided!");

		return inNeighbours[x].begin();
	}

	auto InNeighboursEnd(T x) {
		if (!IsValidVertex(x))
			throw GraphException("[InNeighboursEnd]: Invalid vertex provided!");

		return inNeighbours[x].end();
	}
};