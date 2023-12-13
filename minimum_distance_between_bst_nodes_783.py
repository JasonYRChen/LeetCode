# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            if node.left:
                yield from inorder(node.left)
            yield node.val
            if node.right:
                yield from inorder(node.right)
        

        current_value = -10 ** 6
        min_diff = float('inf')
        for val in inorder(root):
            min_diff = min(min_diff, val - current_value)
            current_value = val
        return min_diff
