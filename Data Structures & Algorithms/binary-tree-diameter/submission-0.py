# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = 0

        def dfs(node):
            nonlocal diam
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            diam = max(diam, left+right)
            return 1 + max(left, right)
        dfs(root)
        return diam