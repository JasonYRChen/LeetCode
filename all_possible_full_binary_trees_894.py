# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n == 1:
            return [TreeNode()]

        combinations = []
        for m in range(1, n - 1, 2):
            lefts = self.allPossibleFBT(m)
            rights = self.allPossibleFBT(n - 1 - m)
            for left in lefts:
                for right in rights:
                    combinations.append(TreeNode(left=left, right=right))
        return combinations
