# (())())
#(((( ) ( ))( )
#()()()()(()()())()
a = int(input())

for i in range(a):
    galho = input()
    stack = []
    
    for g in galho:
        if g == '(':
            stack.append(g)
        else:
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(g)
    
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")