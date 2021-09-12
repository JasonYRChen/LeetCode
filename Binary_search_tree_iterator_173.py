# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        def inorder(node):
            if node.left:
                yield from inorder(node.left)
            yield node.val
            if node.right:
                yield from inorder(node.right)
        
        self.root = root
        self.data = [num for num in inorder(self.root)]
        self.ith = 0 

    def next(self) -> int:
        self.ith += 1
        return self.data[self.ith-1]

    def hasNext(self) -> bool:
        return self.ith < len(self.data)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
