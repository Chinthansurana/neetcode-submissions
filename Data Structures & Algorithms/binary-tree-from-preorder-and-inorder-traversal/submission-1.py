# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ind = {e:i for i,e in enumerate(inorder)}
        prev = 0

        def build(l,r):
            nonlocal prev
            if l > r:
                return None
            node = TreeNode(preorder[prev])
            index = ind[preorder[prev]]
            prev += 1
            node.left = build(l, index-1)
            node.right = build(index+1, r)
            return node
        return build(0, len(inorder)-1)

        