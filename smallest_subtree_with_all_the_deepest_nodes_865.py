# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node, path: list):
            path.append(node)
            if node.left:
                yield from dfs(node.left, path)
            if node.right:
                yield from dfs(node.right, path)
            if not node.left and not node.right:
                yield path
            path.pop()


        deepest_path = []
        subtree = None
        for path in dfs(root, []):
            if len(path) > len(deepest_path):
                deepest_path = path.copy()
                subtree = deepest_path[-1]
            elif len(path) == len(deepest_path):
                for i in range(len(path)-1, -1, -1):
                    if deepest_path[i] == path[i]:
                        subtree = deepest_path[i]
                        break
        return subtree
