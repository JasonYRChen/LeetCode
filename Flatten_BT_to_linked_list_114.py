# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    PREV = None
    
    def flatten(self, root: TreeNode) -> None:
        if root is None:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        self.PREV, root.left, root.right = root, None, self.PREV

#    # Another solution: do the inverse of preorder
#    def flatten(self, root: TreeNode) -> None:
#        head = TreeNode()
#	if root:
#	    for node in self.inverse_preorder(root):
#	        node.left = None
#	        head.right, node.right = node, head.right
#
#    def inverse_preorder(self, node):
#        if node.right:
#            yield from self.inverse_preorder(node.right)
#	if node.left:
#	    yield from self.inverse_preorder(node.left)
#	yield node

    
#     def flatten(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         head = prev = TreeNode()
#         for node in self.preorder(root):
#             prev.left = node
#             prev = node
#         prev = head
#         while prev.left:
#             prev.left, prev.right = None, prev.left
#             prev = prev.right

#     def preorder(self, node):
#         if node:
#             yield node
#             if node.left:
#                 yield from self.preorder(node.left)
#             if node. right:
#                 yield from self.preorder(node.right)
        
