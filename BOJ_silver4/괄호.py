# 스택 / 큐
def solution(n):
    answer = 0

    # qeueu = []
    # n_list = list(n)

    # for i in range(len(n_list)):
    #     qeueu.append(n_list[i])
    #     if len(qeueu) >= 2 and qeueu[-1] == ')' and qeueu[-2] == '(':
    #         qeueu.pop()
    #         qeueu.pop()
            

    # print(qeueu[-2])

    qeueu = []
    #n_list = list(n)

    for i in n:
        if i == '(':
            qeueu.append(i)
        elif i== ')':
            if qeueu:
                qeueu.pop()
            else:
                return "NO"
    else:
        if not qeueu:
            return "YES"
        else:
            return "NO"

    #return answer

print(solution('(()())((()))'))
