# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = 0
        result, stack = [], [root] if root else []
        while stack:
            temp = []
            result.append([])
            while stack:
                node = stack.pop()
                result[-1].append(node.val)
                if level % 2:
                    if node.right:
                        temp.append(node.right)
                    if node.left:
                        temp.append(node.left)
                else:
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)
            stack = temp
            level += 1
        return result

