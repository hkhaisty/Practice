#pragma once
#include "Node.h"

class SinglyLinkedList
{
public:
	SinglyLinkedList(int rootValue);
	SinglyLinkedList(Node* root);
	Node* root;
	void appendToTail(int value);
	void deleteNode(int value);
	Node* popNode(int value);
};

