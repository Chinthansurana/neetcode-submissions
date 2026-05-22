class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        crsMap = defaultdict(list)
        for crs, pre in prerequisites:
            crsMap[crs].append(pre)
        visited = set()
        seen = set()
        res = []
        def dfs(crs):
            if crs in seen:
                return False
            if crs in visited:
                return True
            seen.add(crs)
            for nei in crsMap[crs]:
                if not dfs(nei):
                    return False
            seen.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
