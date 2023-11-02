# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        second = -1
        dq = deque([root])
        while dq:
            for _ in range(len(dq)):
                node = dq.popleft()
                if root.val < node.val < second or (second == -1 and root.val < node.val):
                    second = node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return second
