#include "Chapter1.h"

bool Chapter1::isUnique(std::string s)
{
	if (s.empty())
	{
		return false;
	}

	std::unordered_map<char, int> characters;
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

bool Chapter1::isUniqueNoExtraDataStructure(std::string s)
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

bool Chapter1::isPermutationXor(std::string s1, std::string s2)
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

void Chapter1::urlify(std::string& s, int trueLength)
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

bool Chapter1::isPermutationOfPalindromeHashTable(std::string s)
{
	if (s.empty())
	{
		return false;
	}

	auto oddCount = 0;
	std::unordered_map<char, int> characterCount;
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

bool Chapter1::isPermutationOfPalindromeBitVector(std::string s)
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

bool Chapter1::isOneEditAway(std::string s1, std::string s2)
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

std::string Chapter1::compressString(std::string s)
{
	std::string result;
	result.reserve(s.length() * 2);
	for (auto i = 0, j = 0; i < s.length(); i = j)
	{
		auto charCount = 0;
		while(s[i] == s[j])
		{
			charCount++;
			j++;
		}
		result += s[i] + std::to_string(charCount);
	}

	return result.length() < s.length() ? result : s;
}

void Chapter1::rotateMatrix(std::vector<std::vector<int>>& matrix)
{

}

void Chapter1::zeroMatrix(std::vector<std::vector<int>>& matrix)
{
	for (auto i = 0; i < matrix.size(); i++)
	{
		for (auto j = 0; j < matrix[i].size(); j++)
		{
			if (matrix[i][j] == 0)
			{
				for (auto& row : matrix)
				{
					row[j] = -1;
				}

				for (auto& element : matrix[i])
				{
					element = -1;
				}
			}
		}
	}

	for (auto& row : matrix)
	{
		for (auto& element : row)
		{
			if (element == -1)
			{
				element = 0;
			}
		}
	}
}

bool Chapter1::isStringRotation(std::string s1, std::string s2)
{
	if (s1.length() != s2.length() || s1.empty() || s2.empty())
	{
		return false;
	}

	return isSubstring(s1 + s1, s2);
}

bool Chapter1::isSubstring(std::string s1, std::string s2)
{
	for (auto i = 0; i < s1.length() - s2.length(); i++)
	{
		if (s1.substr(i, s2.length()) == s2)
		{
			return true;
		}
	}

	return false;
}




