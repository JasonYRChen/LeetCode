"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        order = []
        if root:
            order.append(root.val)
            for child in root.children:
                order.extend(self.preorder(child))
        return order
