# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inverse_inorder(node, total):
            if node.right:
                total = inverse_inorder(node.right, total)
            total += node.val
            node.val = total
            if node.left:
                total = inverse_inorder(node.left, total)
            return total


        inverse_inorder(root, 0)
        return root
