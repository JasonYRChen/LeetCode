""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # DFS
        max_depth = 0
        if root:
            max_depth = 1
            for child in root.children:
                max_depth = max(max_depth, self.maxDepth(child)+1)
        return max_depth


#        # BFS
#        depth = 0
#        if root:
#            dq = deque([root])
#            while dq:
#                depth += 1
#                for _ in range(len(dq)):
#                    node = dq.popleft()
#                    if node.children:
#                        dq.extend(node.children)
#        return depth
