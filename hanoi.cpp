#include <iostream> 
using namespace std;

int cnt = 0; // 이동 횟수에 이용.

void Hanoi(int n, char from, char temp, char to)
// n : 원반개수, from : 원래 위치, temp : 임시 장소, to :목적지
{
	if (n == 1) {
		++cnt;
		cout << "원판 1을" << from << "에서 " << to << "로 이동\n";
	}
	else
	{
		Hanoi(n - 1, from, to, temp); //hanoi 함수를 재귀하고 있다 A에서 C로 이동
		cout << "원판 " << n << "을" << from << "에서 " << to << "로 이동\n";
		++cnt;
		Hanoi(n - 1, temp, from, to); //B에서 C로 이동
	}

}


void main()
{
	int n; //원반의 수

	cout << "원반의 갯수를 입력하세요 : ";
	cin >> n;

	Hanoi(n, 'A', 'B', 'C');    // n개의 원반을 'A'에서 'C'로 이동

	cout << "전체 원반 이동 수(원반수 : " << n << ") = " << cnt << endl;
}
//
