#include "stdafx.h"
#include "../CCI/Chapter1.h"

TEST_CLASS(TestChapter1)
{
public:
	TEST_METHOD(testIsUnique)
	{
		string emptyString;
		string nonUniqueString = "10%#@@ll1";
		string uniqueString = "aZnH56&^sT1Ol0@";

		Assert::IsFalse(Chapter1::isUnique(emptyString));
		Assert::IsFalse(Chapter1::isUnique(nonUniqueString));
		Assert::IsTrue(Chapter1::isUnique(uniqueString));
	}

	TEST_METHOD(testIsUniqueNoExtraDataStructure)
	{
		string emptyString;
		string nonUniqueString = "10%#@@ll1";
		string uniqueString = "aZnH56&^sT1Ol0@";

		Assert::IsFalse(Chapter1::isUniqueNoExtraDataStructure(emptyString));
		Assert::IsFalse(Chapter1::isUniqueNoExtraDataStructure(nonUniqueString));
		Assert::IsTrue(Chapter1::isUniqueNoExtraDataStructure(uniqueString));
	}

	TEST_METHOD(testIsPermutationXOR)
	{
		string emptyString;
		string shortString = "cat533%";
		string longString = "@strL0n64llTT712";
		string otherLongString = "217TTlln0Lstr46@";

		Assert::IsFalse(Chapter1::isPermutationXor(emptyString, shortString));
		Assert::IsFalse(Chapter1::isPermutationXor(shortString, longString));
		Assert::IsFalse(Chapter1::isPermutationXor(longString, emptyString));
		Assert::IsTrue(Chapter1::isPermutationXor(longString, otherLongString));
	}

	TEST_METHOD(testUrlify)
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

	TEST_METHOD(testIsPermutationOfPalindromeHashTable)
	{
		string emptyString;
		string validString = "aaBB cc 333";
		string invalidString = "bb 55cCc66666";

		Assert::IsFalse(Chapter1::isPermutationOfPalindromeHashTable(emptyString));
		Assert::IsTrue(Chapter1::isPermutationOfPalindromeHashTable(validString));
		Assert::IsFalse(Chapter1::isPermutationOfPalindromeHashTable(invalidString));
	}

	TEST_METHOD(testIsPermutationOfPalindromeBitVector)
	{
		string emptyString;
		string validString = "aaBB cc 333";
		string invalidString = "bb 55cCc66666";

		Assert::IsFalse(Chapter1::isPermutationOfPalindromeBitVector(emptyString));
		Assert::IsTrue(Chapter1::isPermutationOfPalindromeBitVector(validString));
		Assert::IsFalse(Chapter1::isPermutationOfPalindromeBitVector(invalidString));
	}

	TEST_METHOD(testIsOneEditAway)
	{
		string ark = "ark";
		string park = "park";
		string dark = "dark";
		string bard = "bard";
		string parks = "parks";

		Assert::IsFalse(Chapter1::isOneEditAway(ark, parks));
		Assert::IsFalse(Chapter1::isOneEditAway(dark, parks));
		Assert::IsFalse(Chapter1::isOneEditAway(bard, dark));
		Assert::IsFalse(Chapter1::isOneEditAway(park, bard));
		Assert::IsTrue(Chapter1::isOneEditAway(ark, park));
		Assert::IsTrue(Chapter1::isOneEditAway(ark, dark));
		Assert::IsTrue(Chapter1::isOneEditAway(park, dark));
		Assert::IsTrue(Chapter1::isOneEditAway(park, parks));
	}

	TEST_METHOD(testCompressString)
	{
		string emptyString = "";
		string willCompress = "aabcccccaaa";
		string wontCompress = "abcd";
		string longCompress = "AAAAAAAAAAAABBBBBBBBBBBccccccccZZZZZeeeeeLLLLL";
		
		string willCompressExpected = "a2b1c5a3";
		string longCompressExpected = "A12B11c8Z5e5L5";

		Assert::AreEqual(emptyString, Chapter1::compressString(emptyString));
		Assert::AreEqual(willCompressExpected, Chapter1::compressString(willCompress));
		Assert::AreEqual(wontCompress, Chapter1::compressString(wontCompress));
		Assert::AreEqual(longCompressExpected, Chapter1::compressString(longCompress));
	}
};
