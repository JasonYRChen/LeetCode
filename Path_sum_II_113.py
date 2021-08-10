# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        return [result for result in self.paths(root, targetSum)]

    def paths(self, node, target):
        if node is not None:
	    if node.left is None and node.right is None and node.val == target:
	        yield [target]
	    for left in self.paths(node.left, target-node.val):
	        yield [node.val] + left
	    for right in self.paths(node.right, target-node.val):
	        yield [node.val] + right

