# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        root_val, l_val, r_val = root.val, min(p.val, q.val), max(p.val, q.val)
        if l_val <= root_val <= r_val:
            return root

        root = root.left if r_val < root_val else root.right
        return self.lowestCommonAncestor(root, p, q)

