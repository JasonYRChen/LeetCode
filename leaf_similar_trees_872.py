# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def preorder(node):
            if not node.left and not node.right:
                yield node.val
            if node.left:
                yield from preorder(node.left)
            if node.right:
                yield from preorder(node.right)


        for leaf1, leaf2 in zip_longest(preorder(root1), preorder(root2)):
            if leaf1 != leaf2:
                return False
        return True
