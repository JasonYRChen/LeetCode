"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root
        while node:
            head = to_connect = Node()
            while node:
                for child in [node.left, node.right]:
                    if child:
                        to_connect.next = child
                        to_connect = child
                node = node.next
            node = head.next
        return root
