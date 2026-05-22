class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        pacif, atlan = set(), set()
        rows, cols = len(heights), len(heights[0])
        def dfs(r, c, visit, prev):
            if (r<0 or r == rows or c<0 or c==cols or (r,c) in visit or heights[r][c] < prev):
                return
            visit.add((r,c))
            neigh = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for (nr,nc) in neigh:
                dfs(nr, nc, visit, heights[r][c])
            
        for c in range(cols):
            dfs(0, c, pacif, heights[0][c])
            dfs(rows-1, c, atlan, heights[rows-1][c])

        for r in range(rows):
            dfs(r, 0, pacif, heights[r][0])
            dfs(r, cols-1, atlan, heights[r][cols-1])

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacif and (r,c) in atlan:
                    res.append([r,c])
        return res

