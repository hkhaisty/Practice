#include "Chapter2.h"

Node* Chapter2::kthToLastElementIterative(SinglyLinkedList list, int k)
{
	auto slow = list.root, fast = list.root;
	for (auto i = 0; i < k; i++)
	{
		if (!fast)
		{
			return nullptr;
		}

		fast = fast->next;
	}

	while (fast)
	{
		fast = fast->next;
		slow = slow->next;
	}

	return slow;
}

Node* Chapter2::kthToLastElementRecursive(SinglyLinkedList list, int k)
{
	auto index = 0;
	return kthToLastElementHelper(list.root, k, index);
}

Node* Chapter2::kthToLastElementHelper(Node* node, int k, int& index)
{
	if (!node)
	{
		return nullptr;
	}

	auto nextNode = kthToLastElementHelper(node->next, k, index);

	index += 1;
	if (index == k)
	{
		return node;
	}

	return nextNode;
}

