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
        # Solution 1. no extra space usage
        if root is not None and root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)
        return root

#        # Solution 2. Use deque with dynamic space usage, not O(1)
#        dq = deque([root]) if root else None
#        while dq:
#            prev_node = Node()
#            for _ in range(len(dq)):
#                curr_node = dq.popleft()
#                if curr_node.left:
#                    dq.append(curr_node.left)
#                    dq.append(curr_node.right)
#                prev_node.next = curr_node
#                prev_node = curr_node
#        return root

