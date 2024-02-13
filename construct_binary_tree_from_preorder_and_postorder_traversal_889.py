# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        preorder, postorder = preorder[1:], postorder[:-1]
        if preorder:
            index = postorder.index(preorder[0]) + 1
            root.left = self.constructFromPrePost(preorder[:index], postorder[:index])
            root.right = self.constructFromPrePost(preorder[index:], postorder[index:])
        return root
