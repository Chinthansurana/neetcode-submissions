class unionfind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = unionfind(len(accounts))
        emailtoind = defaultdict(int)

        for i, emails in enumerate(accounts):
            for email in emails[1:]:
                if email in emailtoind:
                    uf.union(i, emailtoind[email])
                else:
                    emailtoind[email] = i
                
        groups = defaultdict(list)
        for email, ind in emailtoind.items():
            leader = uf.find(ind)
            groups[leader].append(email)

        res = []
        for i, emails in groups.items():
            res.append([accounts[i][0]] + sorted(emails))
        return res       