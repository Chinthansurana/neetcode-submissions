class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacif, atlan = set(), set()
        res = []
        def dfs(row, col, visit, prevheight):
            if ((row, col) in visit or
                row < 0 or col < 0 or row == m or col == n or
                heights[row][col] < prevheight):
                return
            visit.add((row,col))
            dfs(row+1, col, visit, heights[row][col])
            dfs(row-1, col, visit, heights[row][col])
            dfs(row, col+1, visit, heights[row][col])
            dfs(row, col-1, visit, heights[row][col])
        
        for c in range(n):
            dfs(0, c, pacif, heights[0][c])
            dfs(m-1, c, atlan, heights[m-1][c])
        
        for r in range(m):
            dfs(r, 0, pacif, heights[r][0])
            dfs(r, n-1, atlan, heights[r][n-1])

        for r in range(m):
            for c in range(n):
                if (r,c) in pacif and (r,c) in atlan:
                    res.append([r,c])
        return res
