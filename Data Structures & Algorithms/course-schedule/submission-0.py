class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = defaultdict(list)
        for crs, pre in prerequisites:
            courseMap[crs].append(pre)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if courseMap[crs] == []:
                return True
            visited.add(crs)
            for nei in courseMap[crs]:
                if not dfs(nei):
                    return False
            visited.remove(crs)
            courseMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True