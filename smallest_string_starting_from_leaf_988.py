# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def yield_string(node, curr_str=''):
            curr_str = chr(ord('a') + node.val) + curr_str
            if node.left is None and node.right is None:
                yield curr_str
            if node.left:
                yield from yield_string(node.left, curr_str)
            if node.right:
                yield from yield_string(node.right, curr_str)
        
        return min([s for s in yield_string(root)])
