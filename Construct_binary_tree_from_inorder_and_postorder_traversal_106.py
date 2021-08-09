# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_dict = {val: i for i, val in enumerate(inorder)}
        return self.build(postorder, inorder, inorder_dict, len(inorder)-1, 0, len(inorder))

    def build(self, postorder, inorder, inorder_dict, idx_post, start_in, end_in):
        if start_in == end_in:
            return None
        val = postorder[idx_post]
        idx_in = inorder_dict[val]
        node = TreeNode(val)
        left = self.build(postorder, inorder, inorder_dict, idx_post-(end_in-idx_in), start_in, idx_in)
        right = self.build(postorder, inorder, inorder_dict, idx_post-1, idx_in+1, end_in)
        node.left, node.right = left, right
        return node 

