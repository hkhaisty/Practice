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

bool Chapter1::isPermutationPalindrome(string s)
{
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

