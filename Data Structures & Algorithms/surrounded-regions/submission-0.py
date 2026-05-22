class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # 1. Check and capture the border
        # 2. Check and capture the elements inside the border
        # 3. Check and uncapture elements on the border

        m, n = len(board), len(board[0])

        def capture(r,c):
            if (r < 0 or r == m or c < 0 or c == n or board[r][c] != "O"):
                return
            board[r][c] = "T"
            directions = [(r+1, c),(r-1, c),(r, c+1),(r, c-1)]
            for (nr, nc) in directions:
                capture(nr, nc)
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O" and (r in [0, m-1] or c in[0, n-1]):
                    capture(r,c)
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == "T":
                    board[r][c] = "O"
