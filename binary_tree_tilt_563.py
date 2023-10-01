# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def sum_tilt(node):
            if node is None:
                return 0, 0
            
            left_sum, left_tilt = sum_tilt(node.left)
            right_sum, right_tilt = sum_tilt(node.right)
            return left_sum + right_sum + node.val, abs(left_sum - right_sum) + left_tilt + right_tilt

        
        return sum_tilt(root)[1]
