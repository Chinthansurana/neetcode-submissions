class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):
            q = deque([(r,c)])
            visited.add((r,c))

            while q:
                i, j = q.popleft()
                nei = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in nei:
                    nr, nc = i+dr, j+dc

                    if 0<=nr<m and 0<=nc<n and grid[nr][nc] != "0" and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
        
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and (r,c) not in visited:
                    res += 1
                    bfs(r, c)
        return res