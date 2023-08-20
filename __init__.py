class Calcul:
    def __init__(self, first, second) -> None:
        self.first = first
        self.second = second

    # 이렇게 데이터를 설정해 주는 함수를 만들어 주기 보다 생성자를 활용하여 초기값을 설정하는게 안전한다.
    # setdata 함수 없이도 add 함수는 __init__을 통해 할당된 숫자들로 연산이 가능하다.
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

a = Calcul(5,3)
print(a.first) # 5
print(a.add()) # 8