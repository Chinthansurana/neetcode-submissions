class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set() 
        res = []
        def dfs(row, col, visit, prevheights):
            if ((row,col) in visit or row<0 or row==m or col<0 or col == n or heights[row][col] < prevheights):
                return
            visit.add((row,col))
            neigh = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
            for (nr, nc) in neigh:
                dfs(nr, nc, visit, heights[row][col])

        for c in range(n):
            dfs(0, c, pacific, heights[0][c])
            dfs(m-1, c, atlantic, heights[m-1][c])
        
        for r in range(m):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, n-1, atlantic, heights[r][n-1])
        
        for r in range(m):
            for c in range(n):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res



