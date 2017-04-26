#pragma once

// Interface class for the Graph
template<typename T>
class IGraph
{
public:
	virtual void AddEdge(T x,T y) = 0;
	virtual void AddVertex(T x) = 0;
	virtual int CountVertices() const = 0;
	virtual bool IsEdge(T x, T y) = 0;
	virtual void RemoveEdge(T x, T y) = 0;
};