# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # BFS
        dq = deque([root])
        while dq:
            length = len(dq)
            for i in range(length):
                node = dq.popleft()
                if not i:
                    value = node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return value
