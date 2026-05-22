
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])

        def dfs(r,c):
            queue = deque([(r,c)])
            grid[r][c] == "0"
            while queue:
                dr, dc = queue.popleft()
                neighbors = [(dr+1,dc),(dr-1,dc),(dr,dc+1),(dr,dc-1)]
                for (nr,nc) in neighbors:
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc] == "1":
                        queue.append((nr,nc))
                        grid[nr][nc] = "0"

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    dfs(r,c)
                    res +=1

        return res