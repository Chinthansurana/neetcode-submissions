class dsu:
    def __init__(self, n: int):
        self.parent: List[int] = list(range(n))
        self.rank: List[int] = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) # Path Compression
        return self.parent[x]
    
    def union(self, x1: int, x2: int) -> bool:
        p1: int = self.find(x1)
        p2: int = self.find(x2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        uf = dsu(n)
        for u,v in edges:
            if not uf.union(u, v):
                return False
        return True
        
