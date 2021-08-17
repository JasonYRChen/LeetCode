# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root) -> int:
        def dfs(node):
            nonlocal max_value

            left = dfs(node.left) if node.left else float('-inf')
            right = dfs(node.right) if node.right else float('-inf')
            max_value = max(left+right+node.val, left, right, max_value)
            return max(node.val, node.val+left, node.val+right)

        max_value = float('-inf')
        return max(dfs(root), max_value)

# class Solution:
#    MAX_VAL = float('-inf')
#
#    def maxPathSum(self, root) -> int:
#        # The key here is that 'self.MAX_VAL' must come after 'self.dfs(root)'
#        # Otherwise, the max function always read the original MAX_VAL and not renew it
#        return max(self.dfs(root), self.MAX_VAL)
#
#    def dfs(self, node):
#        left = self.dfs(node.left) if node.left else float('-inf')
#        right = self.dfs(node.right) if node.right else float('-inf')
#        self.MAX_VAL = max(left+right+node.val, left, right, self.MAX_VAL)
#        return max(node.val, node.val+left, node.val+right)

