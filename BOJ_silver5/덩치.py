# 나의 등수를 어떻게 정할 것인지에 집중하기
# 힌트를 보고 풀이함

people = int(input())

people_spc = []

for _ in range(people):
    weight, height = list(map(int, input().split()))
    people_spc.append((weight, height))

print(people_spc)

rank_list = []

for p1 in people_spc:
    rank = 1
    for p2 in people_spc:
        if p1[0] < p2[0] and p1[1] < p2[1]:
            rank += 1
    print(rank, end=" ")