#include "stdafx.h"
#include "Chapter1.h"
#include "RandomGenerator.h"

int main()
{
	string test = "Taco Ca";
	cout << boolalpha << Chapter1::isPermutationOfPalindromeHashTable(test) << endl;
	cout << boolalpha << Chapter1::isPermutationOfPalindromeBitVector(test); 
	getchar();

	return 0;
}

