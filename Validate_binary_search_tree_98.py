# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Top-down solution
        return self.check(root)
    
    def check(self, node, low=float('-inf'), high=float('inf')):
        if node is None:
            return True
        if node.val >= high or node.val <= low:
            return False
        return self.check(node.left, low, node.val) and self.check(node.right, node.val, high)
    
    
#     def isValidBST(self, root: TreeNode) -> bool:
#         # Bottom-up solution
#         return self.value_check(root)[0]
        
#     def value_check(self, node):
#         if node is None:
#             return True, float('inf'), float('-inf')
        
#         left_valid, left_min, left_max = self.value_check(node.left)
#         if not left_valid or left_max >= node.val:
#             return False, None, None
        
#         right_valid, right_min, right_max = self.value_check(node.right)
#         if not right_valid or right_min <= node.val:
#             return False, None, None
        
#         return True, min(left_min, node.val), max(right_max, node.val)
        
