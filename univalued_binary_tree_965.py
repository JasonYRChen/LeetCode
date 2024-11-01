# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if (root.left and root.left.val != root.val) or (root.right and root.right.val != root.val):
            return False

        left, right = True, True
        if root.left:
            left = self.isUnivalTree(root.left)
        if root.right:
            right = self.isUnivalTree(root.right)
        
        if left == right and left:
            return True
        return False
