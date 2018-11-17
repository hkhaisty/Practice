#include "stdafx.h"
#include "Chapter1.h"
#include "RandomGenerator.h"

int main()
{
	string toUrl = "github .com  ";
	Chapter1::urlify(toUrl, 11);
	cout << toUrl;

	getchar();

	return 0;
}

