"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        lmap = {}
        curr = head
        while curr:
            lmap[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            lmap[curr].next = lmap.get(curr.next)
            lmap[curr].random = lmap.get(curr.random)
            curr = curr.next
        return lmap[head]