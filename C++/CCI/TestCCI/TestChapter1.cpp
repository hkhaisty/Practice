#include "stdafx.h"
#include "../CCI/Chapter1.h"

TEST_CLASS(TestChapter1)
{
public:
	TEST_METHOD(TestIsUnique)
	{
		string emptyString;
		string nonUniqueString = "10%#@@ll1";
		string uniqueString = "aZnH56&^sT1Ol0@";

		Assert::IsFalse(Chapter1::isUnique(emptyString));
		Assert::IsFalse(Chapter1::isUnique(nonUniqueString));
		Assert::IsTrue(Chapter1::isUnique(uniqueString));
	}

	TEST_METHOD(TestIsUniqueNoExtraDataStructure)
	{
		string emptyString;
		string nonUniqueString = "10%#@@ll1";
		string uniqueString = "aZnH56&^sT1Ol0@";

		Assert::IsFalse(Chapter1::isUniqueNoExtraDataStructure(emptyString));
		Assert::IsFalse(Chapter1::isUniqueNoExtraDataStructure(nonUniqueString));
		Assert::IsTrue(Chapter1::isUniqueNoExtraDataStructure(uniqueString));
	}

	TEST_METHOD(TestIsPermutationXOR)
	{
		string emptyString;
		string shortString = "cat533%";
		string longString = "@strL0n64llTT712";
		string otherLongString = "217TTlln0Lstr46@";

		Assert::IsFalse(Chapter1::isPermutationXOR(emptyString, shortString));
		Assert::IsFalse(Chapter1::isPermutationXOR(shortString, longString));
		Assert::IsFalse(Chapter1::isPermutationXOR(longString, emptyString));
		Assert::IsTrue(Chapter1::isPermutationXOR(longString, otherLongString));
	}

	TEST_METHOD(TestUrlify)
	{
		string emptyString;
		string withSpaces = "my%20weird%20blog.com";
		string noSpaces = "github.com";
		string testEmptyString;
		string testWithSpaces = "my weird blog.com    ";
		string testNoSpaces = "github.com";

		Chapter1::urlify(testEmptyString, testEmptyString.length());
		Chapter1::urlify(testWithSpaces, testWithSpaces.length() - 4);
		Chapter1::urlify(testNoSpaces, testNoSpaces.length());

		Assert::AreEqual(emptyString, testEmptyString);
		Assert::AreEqual(withSpaces, testWithSpaces);
		Assert::AreEqual(noSpaces, testNoSpaces);
	}

	TEST_METHOD(TestIsPermutationOfPalindromeHashTable)
	{
		string emptyString;
		string validString = "aaBB cc 333";
		string invalidString = "bb 55cCc66666";

		Assert::IsFalse(Chapter1::isPermutationOfPalindromeHashTable(emptyString));
		Assert::IsTrue(Chapter1::isPermutationOfPalindromeHashTable(validString));
		Assert::IsFalse(Chapter1::isPermutationOfPalindromeHashTable(invalidString));
	}

	TEST_METHOD(TestIsPermutationOfPalindromeBitVector)
	{
		string emptyString;
		string validString = "aaBB cc 333";
		string invalidString = "bb 55cCc66666";

		Assert::IsFalse(Chapter1::isPermutationOfPalindromeBitVector(emptyString));
		Assert::IsTrue(Chapter1::isPermutationOfPalindromeBitVector(validString));
		Assert::IsFalse(Chapter1::isPermutationOfPalindromeBitVector(invalidString));
	}

	TEST_METHOD(TestIsOneEditAway)
	{
		string ark = "ark";
		string park = "park";
		string dark = "dark";
		string bard = "bard";
		string parks = "parks";

		Assert::IsFalse(Chapter1::IsOneEditAway(ark, parks));
		Assert::IsFalse(Chapter1::IsOneEditAway(dark, parks));
		Assert::IsFalse(Chapter1::IsOneEditAway(bard, dark));
		Assert::IsFalse(Chapter1::IsOneEditAway(park, bard));
		Assert::IsTrue(Chapter1::IsOneEditAway(ark, park));
		Assert::IsTrue(Chapter1::IsOneEditAway(ark, dark));
		Assert::IsTrue(Chapter1::IsOneEditAway(park, dark));
		Assert::IsTrue(Chapter1::IsOneEditAway(park, parks));
	}
};
