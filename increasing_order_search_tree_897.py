# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node.left:
                yield from inorder(node.left)
            yield node
            if node.right:
                yield from inorder(node.right)


        nodes = [n for n in inorder(root)]
        prev = None
        for _ in range(len(nodes)):
            current = nodes.pop()
            current.left, current.right = None, prev
            prev = current
        return current
