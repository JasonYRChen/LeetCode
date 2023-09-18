# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node.left:
                yield from dfs(node.left)
            yield node.val
            if node.right:
                yield from dfs(node.right)

        
        numbers = [n for n in dfs(root)]
        diff = float('inf')
        for i in range(1, len(numbers)):
            diff = min(diff, numbers[i] - numbers[i-1])
        return diff
