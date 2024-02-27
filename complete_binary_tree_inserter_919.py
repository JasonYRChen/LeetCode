# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        queue = deque([root])
        self.array = []
        while queue:
            node = queue.popleft()
            self.array.append(node)
            if node.left:
                queue.append(node.left)
                if node.right:
                    queue.append(node.right)

    def insert(self, val: int) -> int:
        self.array.append(TreeNode(val))
        length = len(self.array)
        height = floor(log(length, 2))
        child_number = length - 2 ** height
        parent_number, right = divmod(child_number, 2)
        parent_node = self.array[length - child_number - 1 - (2 ** (height-1) - parent_number)]
        if right:
            parent_node.right = self.array[-1]
        else:
            parent_node.left = self.array[-1]
        return parent_node.val

    def get_root(self) -> Optional[TreeNode]:
        return self.array[0]


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
