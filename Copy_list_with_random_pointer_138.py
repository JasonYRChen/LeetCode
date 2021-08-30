"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dummy_head = prev_node = Node(0)
        nodes_dict = {}
        while head:
            if head not in nodes_dict:
                nodes_dict[head] = Node(0)
            current_node = nodes_dict[head]
            prev_node.next = current_node
            current_node.val = head.val
            if head.random and head.random not in nodes_dict:
                nodes_dict[head.random] = Node(0)
            current_node.random = nodes_dict[head.random] if head.random else None
            prev_node = current_node
            head = head.next
        return dummy_head.next

