N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

a_cur = 0
b_cur = 0
cnt = 0
A_num = []
B_num=[]

while(1):
    if A[a_cur] > B[b_cur]:
        # print(cnt+1, end = " ")
        B_num.append(str(cnt+1))
        cnt+=1
        b_cur+=1
    else:
        # print(cnt+1, end = " ")
        A_num.append(str(cnt+1))
        cnt+=1
        a_cur+=1

    if (a_cur == N and b_cur < M):
        # print(1, cnt)
        for i in range(cnt, N+M):
            B_num.append(str(i+1))
        break
    elif (a_cur < N and b_cur == M):
        # print(2)
        for i in range(cnt, N+M):
            A_num.append(str(i+1))
        break
    elif (a_cur == N and b_cur == M):
        # print(3)
        break

print(" ".join(A_num))
print(" ".join(B_num))


        



