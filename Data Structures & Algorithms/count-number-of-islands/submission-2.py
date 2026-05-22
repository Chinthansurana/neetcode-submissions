class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        islands = 0
        def bfs(i,j):
            queue = deque([(i,j)])
            grid[i][j] = "0"
            while queue:
                r, c = queue.popleft()
                neighbors = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
                for (dr, dc) in neighbors:
                    if 0<=dr<row and 0<=dc<col and grid[dr][dc] == "1":
                        queue.append((dr,dc))
                        grid[dr][dc] = "0"
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    islands += 1 
                    bfs(r, c)
        return islands
