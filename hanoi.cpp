#include <iostream> 
using namespace std;

int cnt = 0; // �̵� Ƚ���� �̿�.

void Hanoi(int n, char from, char temp, char to)
// n : ���ݰ���, from : ���� ��ġ, temp : �ӽ� ���, to :������
{
	if (n == 1) {
		++cnt;
		cout << "���� 1��" << from << "���� " << to << "�� �̵�\n";
	}
	else
	{
		Hanoi(n - 1, from, to, temp); //hanoi �Լ��� ����ϰ� �ִ� A���� C�� �̵�
		cout << "���� " << n << "��" << from << "���� " << to << "�� �̵�\n";
		++cnt;
		Hanoi(n - 1, temp, from, to); //B���� C�� �̵�
	}

}


void main()
{
	int n; //������ ��

	cout << "������ ������ �Է��ϼ��� : ";
	cin >> n;

	Hanoi(n, 'A', 'B', 'C');    // n���� ������ 'A'���� 'C'�� �̵�

	cout << "��ü ���� �̵� ��(���ݼ� : " << n << ") = " << cnt << endl;
}