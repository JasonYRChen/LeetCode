# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        in_dict = {num:i for i, num in enumerate(inorder)}
        return self.construct(preorder, inorder, in_dict, 0, 0, len(inorder))
    
    def construct(self, preorder, inorder, in_dict, pre_idx, in_start, in_end):
        if in_start == in_end:
            return None
        number = preorder[pre_idx]
        in_idx = in_dict[number]
        node = TreeNode(number)
        left = self.construct(preorder, inorder, in_dict, pre_idx+1, in_start, in_idx)
        right = self.construct(preorder, inorder, in_dict, pre_idx+1+in_idx-in_start, in_idx+1, in_end)
        node.left, node.right = left, right
        return node

#    # Running time: O(n^2)
#    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#        if not preorder:
#            return None
# 
#        node = TreeNode(preorder[0])
#        index = inorder.index(preorder[0])
#        left = self.buildTree(preorder[1:index+1], inorder[:index])
#        right = self.buildTree(preorder[index+1:], inorder[index+1:])
#        node.left, node.right = left, right
#        return node 

