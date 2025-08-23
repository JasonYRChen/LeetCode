# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, num=0):
            num = num * 2 + node.val
            if node.left:
                yield from dfs(node.left, num)
            if node.right:
                yield from dfs(node.right, num)
            if not node.left and not node.right:
                yield num


        return sum(dfs(root))
