# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque([(root, root.val)])
        res = 0

        while q:
            node, big = q.popleft()
            if node.val >= big:
                res += 1
            new_big = max(big, node.val)
            if node.left:
                q.append((node.left, new_big))
            if node.right:
                q.append((node.right, new_big))
        return res
