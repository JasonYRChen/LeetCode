# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # breadth first
        exist_None = False
        nodes = deque([root])
        while nodes:
            for _ in range(len(nodes)):
                node = nodes.popleft()
                if node is None:
                    exist_None = True
                elif exist_None:
                    return False
                else:
                    nodes.append(node.left)
                    nodes.append(node.right)
        return True
