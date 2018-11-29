#pragma once
#include "Node.h"
#include "SinglyLinkedList.h"
#include <unordered_map>

class Chapter2
{
public:
	static void removeDuplicates(SinglyLinkedList list);
	static void removeDuplicatesNoBuffer(SinglyLinkedList list);
	static Node* kthToLastElementIterative(SinglyLinkedList list, int k);
	static Node* kthToLastElementRecursive(SinglyLinkedList list, int k);
private:
	static Node* kthToLastElementHelper(Node* node, int k, int& index);
};
