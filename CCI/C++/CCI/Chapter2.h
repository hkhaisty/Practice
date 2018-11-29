#pragma once
#include "Node.h"
#include "SinglyLinkedList.h"

class Chapter2
{
public:
	static Node* kthToLastElementIterative(SinglyLinkedList list, int k);
	static Node* kthToLastElementRecursive(SinglyLinkedList list, int k);

private:
	static Node* kthToLastElementHelper(Node* node, int k, int& index);
};
