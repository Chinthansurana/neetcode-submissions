class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = defaultdict(list)
        for crs, pre in prerequisites:
            courseMap[crs].append(pre)
        seen = set()
        def dfs(crs):
            if crs in seen:
                return False
            if courseMap[crs] == []:
                return True
            seen.add(crs)
            for nextc in courseMap[crs]:
                if not dfs(nextc):
                    return False
            seen.remove(crs)
            courseMap[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True