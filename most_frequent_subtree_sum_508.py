# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def sub_sums(node, counter):
            left_sum = right_sum = 0
            if node.left:
                left_sum = sub_sums(node.left, counter)
            if node.right:
                right_sum = sub_sums(node.right, counter)
            total = left_sum + right_sum + node.val
            counter[total] += 1
            return total

        
        counter = defaultdict(int)
        sub_sums(root, counter)
        most_frequent = max(counter.values())
        return [s for s, v in counter.items() if v == most_frequent]
