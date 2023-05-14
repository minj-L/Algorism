def solution(n, people):
    answer = 0

    n_people = []
    for p in people:
        age, name = p.split()
        n_people.append((int(age), name))

    # print(people)
    print(n_people)

    # 전체 정렬을 할 수 없는 문제는 어떤 것을 기준으로 정렬할지 정해주면 된다.
    n_people.sort(key = lambda x: x[0])
    for i in n_people:
        print(i[0], i[1])
    return answer

print(solution(3, ['21 Junkyu','21 Dohyun','20 Sunyoung']))

# 풀이2 시간 많이 걸림
n = int(input())

people = []
for i in range(n):
    age, name = map(str, input().split(" "))
    people.append((int(age), i, name))

people = sorted(people)

for i in range(n):
    print(people[i][0], end = " ")
    print(people[i][2])
#
