class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap = defaultdict(list)
        in_degree = [0] * numCourses
        for u,v in prerequisites:
            courseMap[v].append(u)
            in_degree[u] += 1
        q = deque(ele for ele in range(numCourses) if in_degree[ele] == 0)

        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for nei in courseMap[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
        return res if len(res) == numCourses else []