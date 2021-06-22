# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        depth, nodes = 0, [root] if root else []
        while nodes:
            depth += 1
            temp = []
            while nodes:
                node = nodes.pop()
                if node.left is None and node.right is None:
                    return depth
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            nodes = temp.copy()
        return depth
