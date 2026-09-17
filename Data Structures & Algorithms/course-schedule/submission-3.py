class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        coursemap = defaultdict(list)
        in_degree = [0] * numCourses
        for u, v in prerequisites:
            coursemap[v].append(u)
            in_degree[u] += 1
        q = deque([ele for ele in range(numCourses) if in_degree[ele] == 0])
        
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for nei in coursemap[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
        return len(res) == numCourses