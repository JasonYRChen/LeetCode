# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter(node):
            len_left = len_right = 0
            max_left = max_right = 0
            if node.left:
                max_left, len_left = diameter(node.left)
                len_left += 1
            if node.right:
                max_right, len_right = diameter(node.right)
                len_right += 1
            max_len = max(len_left + len_right, max_left, max_right)
            return max_len, max(len_left, len_right)

        return diameter(root)[0]
