class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        counter = defaultdict(int)
        while stack:
            node = stack.pop()
            counter[node.val] += 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        mode_value = max(counter.values())
        return [k for k, v in counter.items() if v == mode_value]
