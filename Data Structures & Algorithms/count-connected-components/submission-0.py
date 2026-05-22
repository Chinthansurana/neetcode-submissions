class unionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * (n)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = unionFind(n)
        res = n
        for u, v in edges:
            res -= uf.union(u,v)
        return res
        