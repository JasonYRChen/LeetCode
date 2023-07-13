# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        num = 0
        if root.left and not root.left.left and not root.left.right:
            num += root.left.val
        if root.left:
            num += self.sumOfLeftLeaves(root.left)
        if root.right:
            num += self.sumOfLeftLeaves(root.right)
        return num
