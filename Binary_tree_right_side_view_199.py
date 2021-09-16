# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root) -> list:
        stack = [root] if root else []
        ans = []
        while stack:
            ans.append(stack[-1].val)
            temp = []
            while stack:
                node = stack.pop()
                if node.right:
                    temp.append(node.right)
                if node.left:
                    temp.append(node.left)
            stack = temp[::-1]
        return ans
        
