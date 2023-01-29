class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def merge(self, a, b):
        self.parent[self.find(b)] = self.find(a)

N = int(input())
uf = UnionFind(N)


for i in range(n):
    a,b = input().split()
    uf.merge(a, b)
    if uf.find(a) == uf.find(b):
        print("No")
        break
print("Yes")
