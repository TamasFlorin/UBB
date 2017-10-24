#pragma once

/// <summary> Custom Pair class implementation.</summary>
template<typename T1, typename T2>
struct Pair
{
	T1 first;
	T2 second;
public:
	/// <summary> Custom constructor. </summary>
	/// <param name="first"> The first element of the pair.</param>
	/// <param name="second"> The first second of the pair.</param>
	Pair(T1 first, T2 second) : first(first), second(second) {}

	/// <summary> Custom constructor. </summary>
	/// <param name="first"> The first element of the pair.</param>
	Pair(T1 first) : first(first) {}

	// default constructor
	Pair() {}

	bool operator >(const Pair& rhs) const
	{
		return this->first > rhs.first;
	}

	bool operator <(const Pair& rhs)const
	{
		return this->first < rhs.first;
	}

	bool operator==(const Pair& rhs) const
	{
		return this->first == rhs.first;
	}

	bool operator!=(const Pair &rhs) const
	{
		return this->first != rhs.first;
	}
};