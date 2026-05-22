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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = unionFind(n)
        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                edges.append((dist, i, j))
        edges.sort()
        res = 0
        for dist, u, v in edges:
            if uf.union(u,v):
                res += dist
        return res

        