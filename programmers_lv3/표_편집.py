def solution(n, k, cmds):
    # i 번째 키에 i번째의 앞, 뒤 숫자를 저장해 두는 것이다.
    linked_list = {i: [i - 1, i + 1] for i in range(n)}
    table = ['O'] * n
    delete = []

    for cmd in cmds:
        cmd = cmd.split()

        if cmd[0] == 'D':
            for _ in range(int(cmd[1])):
                k = linked_list[k][1] # += 되어야 하니까 next node의 값을 가져온다.

        elif cmd[0] == 'U':
            for _ in range(int(cmd[1])):
                k = linked_list[k][0] # -= 되어야 하니까 next node의 값을 가져온다.

        elif cmd[0] == 'C':
            prev, nxt = linked_list[k] # k = 4 prev = 3 nxt = 5
            table[k] = 'X'
            delete.append((prev, k, nxt))

            if nxt == n: #표의 가장 마지막 행이라면
                k = linked_list[k][0] #바로 윗행을 선택하라
            else:
                k = linked_list[k][1] #아니면 다음행

            if prev == -1:
                linked_list[nxt][0] = prev
            elif nxt == n:
                linked_list[prev][1] = nxt
            else:
                linked_list[prev][1] = nxt
                linked_list[nxt][0] = prev
        else: # cmd[0] == 'Z':
            prev, now, nxt = delete.pop()
            table[now] = 'O'

            if prev == -1:
                linked_list[nxt][0] = now
            elif nxt == n:
                linked_list[prev][1] = now
            else:
                linked_list[prev][1] = now
                linked_list[nxt][0] = now

    return ''.join([x for x in table])
