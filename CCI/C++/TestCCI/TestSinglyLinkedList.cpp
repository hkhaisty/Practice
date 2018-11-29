#include "stdafx.h"
#include "../CCI/SinglyLinkedList.h"

TEST_CLASS(TestSinglyLinkedList)
{
	TEST_METHOD(testAppendNode)
	{
		std::vector<int> values = { 5, 10, 15, 20 };
		auto linkedList = SinglyLinkedList(values[0]);
		for (auto i = 1; i < values.size(); i++)
		{
			linkedList.appendToTail(values[i]);
		}

		auto current(linkedList.root);
		for (auto value : values)
		{
			Assert::AreEqual(value, current->value);
			current = current->next;
		}
	}

	TEST_METHOD(testDeleteNode)
	{
		std::vector<int> values = { 5, 10, 15, 20 };
		auto linkedList = SinglyLinkedList(values[0]);
		for (auto i = 1; i < values.size(); i++)
		{
			linkedList.appendToTail(values[i]);
		}

		for (auto i = 0; i < 2; i++)
		{
			linkedList.deleteNode(values[i]);
		}

		auto current(linkedList.root);
		for (auto i = 2; i < values.size(); i++)
		{
			Assert::AreEqual(values[i], current->value);
			current = current->next;
		}
	}

	TEST_METHOD(testPopNode)
	{
		std::vector<int> values = { 5, 10, 15, 20 };
		auto linkedList = SinglyLinkedList(values[0]);
		for (auto i = 1; i < values.size(); i++)
		{
			linkedList.appendToTail(values[i]);
		}

		for (auto value : values)
		{
			auto node = linkedList.popNode(value);
			Assert::AreEqual(value, node->value);
		}
	}
};

