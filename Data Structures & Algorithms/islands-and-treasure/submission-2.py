class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])

        q = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r,c))
                
        while q:
            r,c = q.popleft()
            direc = ((1,0), (-1,0), (0, 1), (0, -1))

            for dr, dc in direc:
                nr, nc = r+dr, c+dc
                if (0<=nr<m and 0<=nc<n and grid[nr][nc] == 2147483647):
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
            