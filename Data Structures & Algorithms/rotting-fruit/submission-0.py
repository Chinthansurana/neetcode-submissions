class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows, cols = len(grid), len(grid[0])
        time, fresh = 0, 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r,c])
        while q and fresh:
            time += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                neighbors = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
                for (nr, nc) in neighbors:
                    if (nr < 0 or nr == rows or nc < 0 or nc == cols or grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    q.append([nr, nc])
                    fresh -= 1
        return time if not fresh else -1
