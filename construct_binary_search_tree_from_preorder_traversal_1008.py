# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        nodes = []
        for num in preorder:
            node = TreeNode(num)
            if not nodes:
                root = node
            elif num < nodes[-1].val:
                nodes[-1].left = node
            elif num > nodes[-1].val:
                while len(nodes) > 1:
                    if num > nodes[-2].val:
                        nodes.pop()
                    else:
                        break
                nodes[-1].right = node
                nodes.pop()
            nodes.append(node)
        return root
