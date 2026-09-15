class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        visited = set()
        res = 0
        direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c):
            if (r < 0 or r >= m or
                c < 0 or c >= n or 
                (r,c) in visited or
                grid[r][c] == "0"
            ):
                return
            
            visited.add((r,c))

            for dr,dc in (direc):
                dfs(r+dr, c+dc)
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and (r,c) not in visited:
                    res += 1
                    dfs(r,c)
        return res