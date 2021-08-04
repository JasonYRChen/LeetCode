# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        array = [i+1 for i in range(n)]
        return list(self.generate(array))
        
    def generate(self, array):
        if not array:
            yield None
        else:
            for i in range(len(array)):
                for left in self.generate(array[:i]):
                    for right in self.generate(array[i+1:]):
                        yield TreeNode(array[i], left, right)

