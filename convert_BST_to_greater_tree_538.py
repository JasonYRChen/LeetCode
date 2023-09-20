# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    last_val = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            if root.right:
                self.convertBST(root.right)
            root.val += self.last_val
            self.last_val = root.val
            if root.left:
                self.convertBST(root.left)
        return root
