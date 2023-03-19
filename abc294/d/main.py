import sys
sys.setrecursionlimit(10**6)

gone =set()
N, Q = map(int, input().split())

yet_called_num=1
not_gone_min=1
for _ in range(Q):
    query = input().split()
    if (query[0]=="1"):
        # called.add(yet_called_num)
        yet_called_num+=1
    if (query[0]=="2"):
        come = int(query[1])
        # called.remove(come)
        gone.add(come)
        if come==not_gone_min:
            while not_gone_min in gone:
                not_gone_min+=1
    if (query[0]=="3"):
        print(not_gone_min)

    