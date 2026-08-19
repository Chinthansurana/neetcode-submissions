# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        queue = deque([(p,q)])
        while queue:
            l, r = queue.popleft()
            if not l and not r:
                continue
            if not l or not r or l.val != r.val:
                return False
            queue.append((l.left, r.left))
            queue.append((l.right, r.right))
        return True