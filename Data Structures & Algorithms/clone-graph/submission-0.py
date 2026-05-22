"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldtoNew = {}
        oldtoNew[node] = Node(node.val)
        queue = deque([node])

        while queue:
            current = queue.popleft()
            for nei in current.neighbors:
                if nei not in oldtoNew:
                    oldtoNew[nei] = Node(nei.val)
                    queue.append(nei)
                oldtoNew[current].neighbors.append(oldtoNew[nei])
        return oldtoNew[node]