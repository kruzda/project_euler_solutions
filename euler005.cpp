#include <iostream>
typedef unsigned int UINT;
typedef char          _TCHAR;
int main(int argc, _TCHAR* argv[])
{
	UINT NumToTest = 1;
	int j = 0;
	do{
		for (UINT i = 1; i < 21; i++){
			if ( (NumToTest%i==0) && (i==20)){
				std::cout << "result :" << NumToTest;
				return 0;}
			else if (NumToTest%i!=0){break;}
		}
		NumToTest++;
		j++;
	}while (j != -1);
	return 0;
}
