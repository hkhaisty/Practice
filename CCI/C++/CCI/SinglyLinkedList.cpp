#include "SinglyLinkedList.h"


SinglyLinkedList::SinglyLinkedList(int rootValue)
{
	this->root = new Node(rootValue);
}

SinglyLinkedList::SinglyLinkedList(Node* root)
{
	this->root = root;
}

void SinglyLinkedList::appendToTail(int value)
{
	auto current(root);
	while (current->next)
	{
		current = current->next;
	}

	current->next = new Node(value);
}

void SinglyLinkedList::deleteNode(int value)
{
	if (root->value == value)
	{
		root = root->next;
	}

	auto current(root);
	while (current->next)
	{
		if (current->next->value == value)
		{
			auto temp = current->next;
			current->next = current->next->next;
			delete temp;
			break;
		}

		current = current->next;
	}
}

Node* SinglyLinkedList::popNode(int value)
{
	auto current(root);
	if (current->value == value)
	{
		root = current->next;
		return current;
	}

	while (current->next)
	{
		if (current->next->value == value)
		{
			auto popNode = current->next;
			current->next = current->next->next;
			return popNode;
		}

		current = current->next;
	}

	return nullptr;
}


