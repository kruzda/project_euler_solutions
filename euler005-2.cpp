#include <iostream>

bool DivisibleBy20 (int num)
{
	for (int i = 2; i <= 20; i++)
	{
		if (!(num % i == 0))
		{
			return false;
		}
	}
	
	return true;
}

int main ()
{
	int i;
	for (i = 20; !DivisibleBy20(i); i += 20)
		;
	
	std::cout << i << std::endl;
	
	return 0;
}
