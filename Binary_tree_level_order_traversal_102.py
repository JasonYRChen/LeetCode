# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result, in_deck = [], deque([root]) if root else []
        while in_deck:
            result.append([])
            for _ in range(len(in_deck)):
                node = in_deck.popleft()
                result[-1].append(node.val)
                if node.left:
                    in_deck.append(node.left)
                if node.right:
                    in_deck.append(node.right)
        return result

