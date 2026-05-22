class Solution:
    def islandsAndTreasure(self, rooms: List[List[int]]) -> None:
        m, n = len(rooms), len(rooms[0])
        visit = set()
        q = deque()

        def addRooms(i, j):
            if (i<0 or i==m or j<0 or j==n or (i,j) in visit or rooms[i][j] == -1):
                return
            q.append([i,j])
            visit.add((i,j))

        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        depth = 0
        while q:
            for i in range(len(q)):
                cr, cc = q.popleft()
                rooms[cr][cc] = depth
                addRooms(cr+1, cc)
                addRooms(cr-1, cc)
                addRooms(cr, cc+1)
                addRooms(cr, cc-1)
            depth += 1