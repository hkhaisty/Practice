#include "stdafx.h"
#include "Chapter1.h"

bool Chapter1::isUnique(string s)
{
	if (s.empty())
	{
		return false;
	}

	unordered_map<char, int> characters;
	for (auto character : s)
	{
		if (characters[character])
		{
			return false;
		}

		characters[character] = static_cast<int>(character);
	}

	return true;
}

bool Chapter1::isUniqueNoExtraDataStructure(string s)
{
	if (s.empty())
	{
		return false;
	}

	for (auto i = 0; i < s.length(); i++)
	{
		for (auto j = i + 1; j < s.length(); j++)
		{
			if (s[i] == s[j])
			{
				return false;
			}
		}
	}

	return true;	
}

bool Chapter1::isPermutationXor(string s1, string s2)
{
	if (s1.length() != s2.length())
	{
		return false;
	}

	auto foundChars = 0;
	for (auto i = 0; i < s1.length(); i++)
	{
		foundChars ^= s1[i] ^ s2[i];
	}

	return foundChars == 0;
}

void Chapter1::urlify(string& s, int trueLength)
{
	int lastIndex = s.length() - 1;
	for (auto i = trueLength - 1; i >= 0; i--)
	{
		if (s[i] == ' ')
		{
			s[lastIndex] = '0';
			s[lastIndex - 1] = '2';
			s[lastIndex - 2] = '%';
			lastIndex -= 3;
		}
		else
		{
			s[lastIndex] = s[i];
			lastIndex--;
		}
	}
}

bool Chapter1::isPermutationOfPalindromeHashTable(string s)
{
	if (s.empty())
	{
		return false;
	}

	auto oddCount = 0;
	unordered_map<char, int> characterCount;
	for (auto character : s)
	{
		if (character == ' ') continue;

		character = tolower(character);
		if (!characterCount[character])
		{
			characterCount[character] = 0;
		}

		characterCount[character]++;

		oddCount += characterCount[character] % 2 != 0 ? 1 : -1;
	}

	return oddCount <= 1;
}

bool Chapter1::isPermutationOfPalindromeBitVector(string s)
{
	if (s.empty())
	{
		return false;
	}

	auto bitVector = 0;
	for (auto character : s)
	{
		if (character == ' ') 
			continue;

		auto index = tolower(character) - 'a';
		auto mask = 1 << index;
		if ((bitVector & mask) == 0)
		{
			bitVector |= mask;
		}
		else
		{
			bitVector &= ~mask;
		}
	}

	return (bitVector & bitVector - 1) == 0;
}

bool Chapter1::isOneEditAway(string s1, string s2)
{
	if (abs(static_cast<int>(s1.length() - s2.length())) > 1)
	{
		return false;
	}

	auto shorter = s1.length() < s2.length() ? s1 : s2;
	auto longer = shorter == s1 ? s2 : s1;

	auto sIter = shorter.begin(), lIter = longer.begin();
	auto charDiff = 0;
	while (sIter != shorter.end() && lIter != longer.end())
	{
		if (*sIter != *lIter)
		{
			charDiff++;

			if (charDiff > 1)
			{
				return false;
			}

			if (shorter.length() == longer.length())
			{
				++sIter;
			}
		}
		else
		{
			++sIter;
		}

		++lIter;
	}

	return true;
}

string Chapter1::compressString(string s)
{
	string result;
	result.reserve(s.length());
	for (auto i = 0, j = 0; i < s.length(); i = j)
	{
		auto charCount = 0;
		while(s[i] == s[j])
		{
			charCount++;
			j++;
		}
		result += s[i] + to_string(charCount);
	}

	return result.length() < s.length() ? result : s;
}



