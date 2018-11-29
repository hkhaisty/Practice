#include "stdafx.h"
#include "../CCI/SinglyLinkedList.h"
#include "../CCI/Chapter2.h"

TEST_CLASS(TestChapter2)
{
	TEST_METHOD(testRemoveDuplicates)
	{
		std::vector<int> values = { 3, 1, 1, 1, 3, 2, 2, 3 };
		auto linkedList = SinglyLinkedList(values[0]);
		for (auto i = 1; i < values.size(); i++)
		{
			linkedList.appendToTail(values[i]);
		}

		Chapter2::removeDuplicates(linkedList);

		std::vector<int> nonDuplicateValues = { 3, 1, 2 };
		auto current(linkedList.root);
		for (auto value : nonDuplicateValues)
		{
			Assert::AreEqual(value, current->value);
			current = current->next;
		}
	}
	TEST_METHOD(testKthToLastElementIterative)
	{
		std::vector<int> values = { 5, 10, 15, 20, 25 };
		auto linkedList = SinglyLinkedList(values[0]);
		for (auto i = 1; i < values.size(); i++)
		{
			linkedList.appendToTail(values[i]);
		}

		for (auto i = 0; i < values.size(); i++)
		{
			auto kthElement = Chapter2::kthToLastElementIterative(linkedList, values.size() - i);
			Assert::AreEqual(values[i], kthElement->value);
		}
	}

	TEST_METHOD(testKthToLastElementRecursive)
	{
		std::vector<int> values = { 5, 10, 15, 20, 25 };
		auto linkedList = SinglyLinkedList(values[0]);
		for (auto i = 1; i < values.size(); i++)
		{
			linkedList.appendToTail(values[i]);
		}

		for (auto i = 0; i < values.size(); i++)
		{
			auto kthElement = Chapter2::kthToLastElementRecursive(linkedList, values.size() - i);
			Assert::AreEqual(values[i], kthElement->value);
		}
	}
};