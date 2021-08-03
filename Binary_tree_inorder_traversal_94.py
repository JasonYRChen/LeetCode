# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return list(self.inorder(root))
        
    def inorder(self, node):
        if node:
            if node.left:
                yield from self.inorder(node.left)
            yield node.val
            if node.right:
                yield from self.inorder(node.right)

