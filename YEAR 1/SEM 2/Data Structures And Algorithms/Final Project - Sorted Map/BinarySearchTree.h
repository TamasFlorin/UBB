#pragma once

#include "vector.h"

/// <summary> Binary search tree exception class implementation. </summary>
class BinarySearchTreeException : public std::runtime_error
{
public:
	BinarySearchTreeException(const std::string& message) : std::runtime_error(message) {}
};

/// <summary> Templated binary search tree class implementation. </summary>
template<typename T>
class BinarySearchTree
{
protected:
	/// <summary> Node class implementation. </summary>
	struct Node
	{
		T data; // data store in node
		Node *left; // left child
		Node *right; // right child

		/// <summary> Custom Node constructor. </summary>
	    /// <param name="data"> The data that the node will store.</param>
		Node(const T &data) : data(data),left(nullptr),right(nullptr){}
	};

	// tree root
	Node *root;

	// current tree size
	std::size_t currSize;

	// vector that sores all the data in sorted order
	// to allow an easier implementation of the iterator
	Vector<T*> inOrder;

	/// <summary> In order tree traversal. </summary>
	/// <remarks> The class member inOrder will store the in order traversal of the tree. </remarks>
	/// <param name="root"> The root of the binary search tree. </param>
	void in_order_traversal(Node *root)
	{
		if (root == nullptr)
			return;

		in_order_traversal(root->left);
		inOrder.push_back(&root->data);
		in_order_traversal(root->right);
	}

	/// <summary> Find the minimum node of a binary search tree. </summary>
	/// <param name="root"> The root of the binary search tree. </param>
	/// <returns> The minimum node found. </returns>
	Node *find_min_node(Node *node)
	{
		if (node == nullptr)
			return node;

		Node *current = node;

		while (current->left != nullptr)
			current = current->left;

		return current;
	}

	/// <summary> Erase the node containing the given data. </summary>
	/// <param name="root"> The root of the binary search tree. </param>
	/// <param name="root"> The data to be removed. </param>
	/// <returns> The new tree root. </returns>
	Node *erase_node(Node *root, const T&data)
	{
		if (root == nullptr)
			return root;

		// if the key is smaller than the root key,then we have to check the left
		else if (data < root->data)
			root->left = erase_node(root->left, data);
		// check the right subtree
		else if (data > root->data)
			root->right = erase_node(root->right, data);
		// same as root key
		else
		{
			// one child on the left side
			if (root->left == nullptr)
			{
				Node *temp = root->right;
				delete root;
				root = nullptr;
				return temp;
			}
			// one child on the right side
			else if (root->right == nullptr)
			{
				Node* temp = root->left;
				delete root;
				root = nullptr;
				return temp;
			}

			// node with two children
			// find the minimum on the right side
			Node * temp = find_min_node(root->right);

			root->data = temp->data;

			// delete the found node
			root->right = erase_node(root->right, temp->data);
		}

		return root;
	}

	/// <summary> Free the data used by the tree. </summary>
	/// <param name="root"> The root of the binary search tree. </param>
	void destroy(Node *root)
	{
		if (root == nullptr)
			return;

		// destroy left subtree
		destroy(root->left);

		// destroy right subtree
		destroy(root->right);
		
		// free current node memory
		delete root;
	}

	Node *find_node(const T&value)
	{
		if (root == nullptr)
			return root;

		Node *current = root;

		while (current != nullptr && current->data != value) {
			if (value < current->data) {
				current = current->left;
			}
			else {
				current = current->right;
			}
		}

		return current;
	}

public:
	class iterator
	{
	private:
		typedef T value_type;
		typedef T& reference;
		typedef T* pointer;

		pointer * currData;
	public:
		iterator(pointer * ptr) : currData(ptr) {}

		iterator operator++() 
		{
			iterator i = *this; 
			currData++;
			return i;
		}

		iterator operator++(int)
		{
			currData++;
			return *this;
		}

		reference operator *()
		{
			return (*(*currData));
		}

		pointer operator->()
		{
			return *currData;
		}

		pointer get_data()
		{
			return *currData;
		}

		bool operator==(const iterator& rhs) const
		{
			return currData == rhs.currData;
		}

		bool operator!=(const iterator& rhs) const
		{
			return currData != rhs.currData;
		}
	};

	BinarySearchTree() : root(nullptr), currSize(0)
	{

	}

	~BinarySearchTree()
	{
		destroy(root);
	}

	/// <summary> Return the current size of the tree. </summary>
	/// <returns> the size of the tree </returns>
	std::size_t size() const
	{
		return currSize;
	}

	/// <summary> Insert new data in the tree. </summary>
	/// <param name="data"> The data to be inserted </param>
	void insert(const T &data) 
	{
		// increment current tree size
		currSize++;

		// tree is empty
		if (root == nullptr) {
			root = new Node(data);
			return;
		}

		Node *current = root;
		Node *slow = root;

		// find the node where the new data should be inserted
		while (current != nullptr)
		{
			slow = current;

			if (data < current->data)
				current = current->left;
			else
				current = current->right;
		}

		// insert on the right side
		if (data > slow->data)
		{
			slow->right = new Node(data);
		}
		// insert on the left side
		else
			slow->left = new Node(data);
	}

	/// <summary> Remove the given data from the tree. </summary>
	/// <param name="data"> The data to be removed. </param>
	/// <returns> true if the data has been removed,false otherwise. </returns>
	bool erase(const T& data)
	{
		if (!this->search(data))
			return false;

		// erase node
		root = erase_node(this->root, data);

		// decrement tree size
		--currSize;

		return true;
	}

	/// <summary> Returns an iterator for the in order traversal of the tree. </summary>
	/// <returns> iterator to a vector containing the in order traversal of the tree. </returns>
	iterator begin()
	{
		// clear the vector
		inOrder.clear();

		// traverse the tree in order
		in_order_traversal(root);

		// return an iterator to the vector
		return iterator(inOrder.data());
	}

	/// <summary> Returns an iterator for the last element + 1 of the in order traversal.</summary>
	/// <returns> iterator to the last element + 1 of a vector containing the in order traversal of the tree. </returns>
	iterator end()
	{
		return iterator(inOrder.data() + inOrder.size());
	}

	bool search(const T& value)
	{
		return find_node(value) != nullptr;
	}

	T& at(const T& value)
	{
		Node *res = find_node(value);

		if (res == nullptr)
			throw BinarySearchTreeException("Invalid value provided!");

		return res->data;
	}
};