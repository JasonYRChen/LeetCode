# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node:
            new_nodes = {node.val: Node(node.val)}
            queue = [node]
            while queue:
                current_node = queue.pop()
                value = current_node.val
                for neighbor in current_node.neighbors:
                    if neighbor.val not in new_nodes:
                        new_nodes[neighbor.val] = Node(neighbor.val)
                        queue.append(neighbor)
                    new_nodes[value].neighbors.append(new_nodes[neighbor.val])
        return new_nodes[node.val] if node else node

