class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crsMap = defaultdict(list)
        for crs, prereq in prerequisites:
            crsMap[crs].append(prereq)
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if crsMap[crs] == []:
                return True
            visited.add(crs)
            for nei in crsMap[crs]:
                if not dfs(nei):
                    return False
            visited.remove(crs)
            crsMap[crs] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True