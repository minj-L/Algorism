T = int(input())

for _ in range(T):
    galho = input()

    stack = []
    stack2 = []
    
    for g in galho:
        if g == '(':
            stack.append(g)

        if g == ')' and len(stack) != 0:
            stack.pop()
        elif len(stack) == 0 and g == ')':
            stack2.append(g)
    
    if len(stack) == 0 and len(stack2) == 0:
        print("YES")
    else:
        print("NO")