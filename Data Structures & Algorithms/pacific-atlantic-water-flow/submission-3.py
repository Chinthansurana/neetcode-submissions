class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        atla, paci = set(), set()

        def dfs(r, c, visit, prev):
            if (
                r < 0 or
                r >= m or
                c < 0 or
                c >= n or
                (r,c) in visit or
                heights[r][c] < prev
            ):
                return
            visit.add((r,c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
        
        for r in range(m):
            dfs(r, 0, paci, heights[r][0])
            dfs(r, n-1, atla, heights[r][n-1])
        
        for c in range(n):
            dfs(0, c, paci, heights[0][c])
            dfs(m-1, c, atla, heights[m-1][c])
        
        res = []
        for r in range(m):
            for c in range(n):
                if (r,c) in atla and (r,c) in paci:
                    res.append((r,c))
        return res
