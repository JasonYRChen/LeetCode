# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = [root.val] if root else []
        if root and root.left:
            ans.extend(self.preorderTraversal(root.left))
        if root and root.right:
            ans.extend(self.preorderTraversal(root.right))
        return ans 

