class unionFind:
    def __init__(self, N):
        self.parent = list(range(N+1))
        self.rank = [1] * (N+1)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = unionFind(len(edges))
        for u,v in edges:
            if not uf.union(u,v):
                return [u,v]
        return []
        