# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        dq = None if root is None else deque([root])
        max_nums = []
        while dq:
            length = len(dq)
            for i in range(length):
                node = dq.popleft()
                if not i:
                    max_nums.append(node.val)
                else:
                    max_nums[-1] = max(max_nums[-1], node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return max_nums
