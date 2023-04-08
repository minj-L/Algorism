cells = [[0] * 51 for _ in range(51)]
index = 1
# 1부터 키값 할당
for i in range(1, 51):
    for j in range(1, 51):
        cells[i][j] = index
        index += 1
store = {}

def change(r, c, value):
    store[cells[r][c]] = value

def get_target(key):
    targets = []
    for i in range(1, 51):
        for j in range(1, 51):
            if cells[i][j] == key: targets.append([i, j])
    return targets

def update(command):
    # "UPDATE r c value" 형태
    if len(command) == 4:
        ud, r, c, value = command
        r, c = int(r), int(c)
        change(r, c, value)
    # "UPDATE value1 value2" 형태
    if len(command) == 3:
        ud, find_value, change_value = command
        for i in range(1, 51):
            for j in range(1, 51):
                if cells[i][j] in store and store[cells[i][j]] == find_value:
                    change(i, j, change_value)

def merge(command):
    mg, r1, c1, r2, c2 = command
    r1, r2, c1, c2 = int(r1), int(r2), int(c1), int(c2)
    # 같은 좌표의 경우 무시
    if r1 == r2 and c1 == c2: return

    if cells[r1][c1] in store:
        targets = get_target(cells[r2][c2])
        for x, y in targets:
            cells[x][y] = cells[r1][c1]

    elif cells[r2][c2] in store:
        targets = get_target(cells[r1][c1])
        for x, y in targets:
            cells[x][y] = cells[r2][c2]
    else:
        targets = get_target(cells[r2][c2])
        for x, y in targets:
            cells[x][y] = cells[r1][c1]
        

def ummerge(command):
    global index
    um, r, c = command
    r, c = int(r), int(c)

    for i in range(1, 51):
        for j in range(1, 51):
            if i == r and j == c: continue
            if cells[i][j] == cells[r][c]:
                cells[i][j] = index
                index += 1

def print_cell(command):
    pt, r, c = command
    r, c = int(r), int(c)
    
    if cells[r][c] in store:
        return store[cells[r][c]]
    else:
        return "EMPTY"
                
def solution(commands):
    answer = []
    for command in commands:
        command = command.split()
        if command[0] == "UPDATE": update(command)
        elif command[0] == "MERGE": merge(command)
        elif command[0] == "UNMERGE": ummerge(command)
        elif command[0] == "PRINT": 
            answer.append(print_cell(command))

    return answer
#
