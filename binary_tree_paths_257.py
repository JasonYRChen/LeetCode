# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        results = []
        nodes = [root]
        while nodes:
            if nodes[-1].left:
                nodes.append(nodes[-1].left)
            elif nodes[-1].right:
                nodes.append(nodes[-1].right)
            else:
                results.append('->'.join(str(node.val) for node in nodes))
                node = nodes.pop()
                while nodes and (node == nodes[-1].right or nodes[-1].right is None):
                    node = nodes.pop()
                if nodes:
                    nodes.append(nodes[-1].right)
        return results
