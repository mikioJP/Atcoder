import sys
input = sys.stdin.readline

import numpy as np

n=int(input())
inf = 10**6

a=[]
for i in range(n-1):
    a.append(list(map(int, input().split())))

def make_graph(a, n):
    path_map = np.zeros(n**2).reshape(n, n)
    path_map[:,:]=inf

    for i in a:
        st_idx=i[0]-1
        et_idx=i[1]-1
        path_map[st_idx][et_idx]=1
        path_map[et_idx][st_idx] = 1

    return path_map

# path_map=make_graph(a,n)
# print(path_map)
# print(a)

def make_adjacent_list(a, n):
    adjacent_list=[[] for i in range(n)]
    for ary in a:
        adjacent_list[ary[0]-1].append(ary[1])
        adjacent_list[ary[1]-1].append(ary[0])
    return adjacent_list

adjacent_list = make_adjacent_list(a, n)
min_path_list=[inf for i in range(n)]
start=1
min_path_list[start-1] = 0
min_path=0
present_city=start
next_city_list=adjacent_list[present_city-1]
next_city_tmp = next_city_list[0]

print(adjacent_list)

while(1):
    for c in next_city_list:
        if min_path_list[c-1] > min_path_list[present_city-1] + 1:
            min_path_list[c-1] = min_path_list[present_city-1] + 1
            next_city_tmp = c

    print(present_city)
    print(next_city_tmp)
    if present_city!=next_city_tmp:
        present_city=next_city_tmp
        next_city_list = adjacent_list[present_city-1]
    else:
        break
print(min_path_list)
    

