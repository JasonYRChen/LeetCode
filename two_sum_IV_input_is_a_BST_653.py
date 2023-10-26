 Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # O(n) running time, O(n) space
        def dfs(node):
            if node is None:
                return False
            if k - node.val in searched:
                return True
            searched.add(node.val)
            return dfs(node.left) or dfs(node.right)


        searched = set()
        return dfs(root)


        # O(nlogn) running time, O(1) space
#        def nodes(node):
#            yield node
#            if node.left:
#                yield from nodes(node.left)
#            if node.right:
#                yield from nodes(node.right)


#        for node in nodes(root):
#            temp = root
#            target = k - node.val
#            while temp is not None:
#                if temp.val == target and temp != node:
#                    return True
#                if target > temp.val:
#                    temp = temp.right
#                else:
#                    temp = temp.left
#        return False
