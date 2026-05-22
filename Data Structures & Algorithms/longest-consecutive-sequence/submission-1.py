class unionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)
        if p1 != p2:
            if self.size[p1] > self.size[p2]:
                self.parent[p2] = p1
                self.size[p1] += self.size[p2]
            else:
                self.parent[p1] = p2
                self.size[p2] += self.size[p1]
        
    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numset = set(nums)    
        uf = unionFind()
        for num in numset:
            uf.add(num)
        
        for num in numset:
            if (num-1) in numset:
                uf.union(num, num-1)
            if (num+1) in numset:
                uf.union(num, num+1)
        return max(uf.size.values())

