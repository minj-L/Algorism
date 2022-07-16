A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]

if len(A) == 1:
    print(1)

arr = []

for i in range(len(A)):
    arr.append((A[i], B[i]))

arr_ = []
arr_.append(arr[0])

#print(len(arr_))

for i in range(1, len(arr)):
    while(True):
        if arr[i][1] == 0 and arr_[len(arr_)-1][1] == 1:
            if arr[i][0] < arr_[len(arr_)-1][0]:
                break
            else:
                del arr_[len(arr_)-1]
                if len(arr_) == 0:
                    arr_.append(arr[i])
                    break
        else:
            arr_.append(arr[i])
            break
print(len(arr_))

# 보고 풀이  다시 풀기 https://datacodingschool.tistory.com/40
