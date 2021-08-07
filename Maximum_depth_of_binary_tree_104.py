# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root, 1)
        
    def depth(self, node, level):
        if node is None:
            return level - 1
        return max(self.depth(node.left, level+1), self.depth(node.right, level+1))

