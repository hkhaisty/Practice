#include "stdafx.h"
#include "Chapter1.h"
#include "RandomGenerator.h"

int main()
{
	//auto strings = RandomGenerator::generateRandomAsciiStrings(100);
	//for (auto string : strings)
	//{
	//	auto isUnique = Chapter1::isUnique(string);
	//	cout << string << " : " << boolalpha << isUnique << endl;
	//}

	string s1 = "Have. fun at your soccer game";
	string s2 = "Have  fun at your soccer game";
	cout << boolalpha << Chapter1::isPermutation(s1, s2);

	getchar();

	return 0;
}

