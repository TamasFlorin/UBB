#pragma once

#include "BinarySearchTree.h"
#include "Pair.h"

class SortedMapException : public std::runtime_error
{
public:
	SortedMapException(const std::string& message) : std::runtime_error(message) {}
};

template<typename TKey,typename TValue>
class SortedMap 
{
	typedef Pair<TKey, TValue> value_type;

	BinarySearchTree<value_type> bst;
public:
	// iterator class
	class iterator 
	{
		typedef Pair<TKey,TValue>& reference;
		typedef Pair<TKey,TValue>* pointer;
		typedef Pair<TKey, TValue > value_type;

		typename BinarySearchTree<value_type>::iterator bstIterator;
	public:
		iterator(typename BinarySearchTree<value_type>::iterator iter) : bstIterator(iter){}
		
		iterator operator++()
		{
			iterator i = *this;
			bstIterator++;
			return i;
		}

		iterator operator++(int)
		{
			bstIterator++;
			return *this;
		}

		reference operator*()
		{
			return *bstIterator;
		}

		pointer operator ->()
		{
			return bstIterator.get_data();
		}

		bool operator==(const iterator& rhs) const
		{
			return bstIterator == rhs.bstIterator;
		}

		bool operator!=(const iterator& rhs) const
		{
			return bstIterator != rhs.bstIterator;
		}
	};

	/*
	========== Iterators ==========
	*/

	iterator begin()
	{
		return iterator(bst.begin());
	}

	iterator end()
	{
		return iterator(bst.end());
	}

	/* 
	========== Capacity ==========
	*/

	/// <summary> Check if the tree is empty. </summary>
	/// <returns> true if the tree is empty,false otherwise. </returns>
	bool empty() const
	{
		return bst.size() == 0;
	}

	/// <summary> Get the current size of the map. </summary>
	/// <returns> The current size of the map. </returns>
	std::size_t size() const
	{	
		return bst.size();
	}
	
	/*
	========== Element access ==========
	*/
	
	/// <summary> Get the element having a given key. </summary>
	/// <param name="key"> The key of the element to be returned. </param>
	/// <returns> The element having the given key. </returns>
	TValue& at(const TKey& key)
	{
		if (!bst.search(value_type(key)))
			throw SortedMapException("Invalid key!");
		
		return bst.at(value_type(key)).second;
	}

	/// <summary> Return a Vector containing all the <key,data> pairs. </summary>
	Vector<value_type> pairs()
	{
		Vector<value_type> result;

		for (iterator it = this->begin(); it != this->end(); it++)
			result.push_back(*it);

		return result;
	}

	/// <summary> Return a Vector containing all the keys. </summary>
	Vector<TKey> keys()
	{
		Vector<TKey> result;

		for (iterator it = this->begin(); it != this->end(); it++)
			result.push_back((*it).first);

		return result;
	}

	/// <summary> Return a Vector containing all the data. </summary>
	Vector<TValue> values()
	{
		Vector<TValue> result;

		for (iterator it = this->begin(); it != this->end(); it++)
			result.push_back((*it).second);

		return result;
	}

	/*
	========== Modiffiers ==========
	*/

	/// <summary> Add new data(and construct it) to the map. </summary>
	/// <param name="key"> The key of the data to be added. </param>
	/// <param name="value"> The data to be added. </param>
	/// <returns> return a pair, with its member pair::first set to an iterator pointing to either the newly inserted element or 
	/// to the element with an equivalent key in the map. The pair::second element in the pair is set to true if a new element 
	/// was inserted or false if an equivalent key already existed.
	/// </returns>
	bool emplace(const TKey& key, const TValue& value)
	{
		if (bst.search(value_type(key)))
			return false;
		
		bst.insert(value_type(key, value));

		return true;
	}

	/// <summary> Add new data to the map. </summary>
	/// <param name="key"> The key of the data to be added. </param>
	/// <param name="value"> The data to be added. </param>
	/// <returns> return a pair, with its member pair::first set to an iterator pointing to either the newly inserted element or 
	/// to the element with an equivalent key in the map. The pair::second element in the pair is set to true if a new element 
	/// was inserted or false if an equivalent key already existed.
	/// </returns>
	bool insert(const value_type &data)
	{
		return emplace(data.first, data.second);
	}

	/// <summary> Renove data from the map. </summary>
	/// <param name="key"> The key of the data to be removed. </param>
	/// <returns> true if the data has been removed,false otherwise. </returns>
	bool erase(const TKey& key)
	{
		return bst.erase(value_type(key));
	}

	/*
	========== Operations ==========
	*/

	bool search(const TKey &key)
	{
		return bst.search(value_type(key));
	}

};