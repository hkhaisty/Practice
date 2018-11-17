#include "stdafx.h"
#include "RandomGenerator.h"
#include <ctime>


vector<string> RandomGenerator::generateRandomAsciiStrings(int size)
{
	srand(time(nullptr));

	vector<string> strings(size);
	for (auto i = 0; i < size; i++)
	{
		string s;
		for (auto j = 0; j < i + 1; j++)
		{
			s += rand() % (127 - 33) + 33;
		}

		strings[i] = s;
	}

	return strings;
}


