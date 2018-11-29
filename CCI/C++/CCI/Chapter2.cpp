#include "Chapter2.h"

void Chapter2::removeDuplicates(SinglyLinkedList list)
{
	std::unordered_map<int, int> nodeValues;
	auto current(list.root);
	while (current)
	{
		if (nodeValues[current->value])
		{
			auto previous = current->value;
			current = current->next;
			list.deleteNode(previous);
		}
		else
		{
			nodeValues[current->value] = current->value;
			current = current->next;
		}
	}
}

Node* Chapter2::kthToLastElementIterative(SinglyLinkedList list, int k)
{
	auto slow(list.root), fast(list.root);
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

