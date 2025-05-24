# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        prev_node = None
        current_node = root
        while True:
            if current_node is None or current_node.val < val:
                node = TreeNode(val, current_node)
                if prev_node:
                    prev_node.right = node
                return node if current_node == root else root
            prev_node, current_node = current_node, current_node.right
