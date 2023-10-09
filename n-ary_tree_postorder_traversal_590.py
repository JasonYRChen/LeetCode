"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        order = []
        if root:
            for child in root.children:
                order.extend(self.postorder(child))
            order.append(root.val)
        return order
