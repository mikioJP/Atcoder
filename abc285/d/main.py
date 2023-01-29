N=int(input())

p = [-1] * (2*N + 1)
def root(x):
  if p[x] < 0:
    return x
  p[x] = root(p[x])
  return p[x]
 
def unite(x, y):
  x = root(x)
  y = root(y)
  
  if x == y:
    return
  p[x] += p[y]
  p[y] = x

def size(x):
  x = root(x)
  return -p[x]

n=0
fa={}

a,b = input().split()

if a not in fa:
    fa[a]=n
    n+=1
if b not in fa:
    fa[b]=n
    n+=1
unite(fa[a],fa[b])

for i in range(N-1):
    a,b = input().split()
    if a not in fa:
        fa[a]=n
        n+=1
    if b not in fa:
        fa[b]=n
        n+=1
    # print(fa[a], fa[b], fa)
    if root(fa[a])==root(fa[b]):
        print("No")
        exit()
    unite(fa[a],fa[b])
print("Yes")