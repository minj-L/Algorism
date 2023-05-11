def solution(n):
    answer = 0
    beehouse = 1
    how_room = 1

    while n > beehouse:
        beehouse += 6 * how_room
        how_room += 1

    return how_room

print(solution(13))
#
