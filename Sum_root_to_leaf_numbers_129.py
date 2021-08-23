# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root) -> int:
        return sum(self.depth_sum(root, 0))

    def depth_sum(self, node, total):
        if node.left is None and node.right is None:
            yield total + node.val
        else:
            total += node.val
            if node.left:
                yield from self.depth_sum(node.left, total*10)
            if node.right:
                yield from self.depth_sum(node.right, total*10)

