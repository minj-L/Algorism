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
		//return prod; �� �� ���嵵 �� �������� ���� �� �ִ�.

		return (n * factorial(n - 1));
	}
}

void main() {
	int n;
	cout << "���ڸ� �Է��ϼ��� : ";
	cin >> n;
	cout << n <<"! = " << factorial(n) << endl;
}