# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            l_max = l_min = r_max = r_min = node.val
            l_diff = r_diff = 0
            if node.left:
                l_max, l_min, l_diff = dfs(node.left)
            if node.right:
                r_max, r_min, r_diff = dfs(node.right)
            new_max = max(l_max, r_max, node.val)
            new_min = min(l_min, r_min, node.val)
            new_diff = max(abs(node.val - max(l_max, r_max)),
                           abs(node.val - min(l_min, r_min)),
                           l_diff, r_diff
                          )
            return new_max, new_min, new_diff


        _, _, diff = dfs(root)
        return diff
