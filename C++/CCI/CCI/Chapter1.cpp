#include "stdafx.h"
#include "Chapter1.h"

bool Chapter1::isUnique(string s)
{
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

bool Chapter1::isPermutation(string s1, string s2)
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
