# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(node, parent=None, depth=0, group={x, y}):
            if node.val in group:
                yield parent, depth
            if node.left:
                yield from dfs(node.left, node, depth+1)
            if node.right:
                yield from dfs(node.right, node, depth+1)
        

        mapping = {k: v for k, v in dfs(root)}
        if len(mapping) == 2 and len(set(mapping.values())) == 1:
            return True
        return False
