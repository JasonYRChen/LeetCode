# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        argmax = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[argmax]:
                argmax = i

        root = TreeNode(nums[argmax])
        root.left = self.constructMaximumBinaryTree(nums[:argmax])
        root.right = self.constructMaximumBinaryTree(nums[argmax+1:])
        return root
