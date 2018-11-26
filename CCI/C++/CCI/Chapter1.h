#pragma once
#include <string>
#include <vector>
#include <unordered_map>

class Chapter1
{
public:
	static bool isUnique(std::string s);
	static bool isUniqueNoExtraDataStructure(std::string s);
	static bool isPermutationXor(std::string  s1, std::string s2);
	static void urlify(std::string& s, int trueLength);
	static bool isPermutationOfPalindromeHashTable(std::string s);
	static bool isPermutationOfPalindromeBitVector(std::string s);
	static bool isOneEditAway(std::string s1, std::string s2);
	static std::string compressString(std::string s);
	static void rotateMatrix(std::vector<std::vector<int>>& matrix);
	static void zeroMatrix(std::vector<std::vector<int>>& matrix);
	static bool isStringRotation(std::string s1, std::string s2);
private:
	static bool isSubstring(std::string s1, std::string s2);
};
