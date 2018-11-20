#include "stdafx.h"
#include "Chapter1.h"
#include "RandomGenerator.h"

int main()
{
	string s1 = "pale";
	string s2 = "bake";

	cout << boolalpha << Chapter1::areOneEditAway(s1, s2);
	getchar();

	return 0;
}

