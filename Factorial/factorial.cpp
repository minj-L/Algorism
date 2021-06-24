#include <iostream>
using namespace std;

/* int factorial(int n) // n! = n *(n-1)!, n>1, 1! = 1, 0! = 1
{
	int prod = 1;

	for (int i = 1; i <= n; i++) // n! = 1 * 2 * 3 *...* n
		prod = prod * i;
	
	return (prod);
} */

int factorial(int n)
{
	if (n < 0) cout << "ERROR!";
	if (n == 0) return (1);
	else if (n == 1) return (1);
	else // if (n > 1)
	{
		//int prod = n * factorial(n - 1);
		//return prod; 이 두 문장도 한 문장으로 줄일 수 있다.

		return (n * factorial(n - 1));
	}
}

void main() {
	int n;
	cout << "숫자를 입력하세요 : ";
	cin >> n;
	cout << n <<"! = " << factorial(n) << endl;
}
