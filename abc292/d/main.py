from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

N, M = map(int, input().split())

uf = UnionFind(N)

cycle_cnt=defaultdict(int)

for _ in range(M):
    u, v = map(int, input().split())
    u-=1
    v-=1

    par_u = uf.find(u)
    par_v = uf.find(v)

    # すでに同じグループの場合は一回のみ追加されていなければならない
    if (par_u == par_v):
        cycle_cnt[par_u]+=1
    
    uf.union(u, v)

cycle_ans=defaultdict(int)

for k, v in cycle_cnt.items():
    cycle_ans[uf.find(k)]+=v

for root in uf.roots():
    if cycle_ans[root]!=1:
        print("No")
        exit()
print("Yes")
