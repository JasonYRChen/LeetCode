class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        gen = self.inorder(root)
        prev = next(gen)
        mistake1, mistake2 = None, None
        for node in gen:
            if prev.val > node.val:
                if mistake1 is None:
                    mistake1 = prev
                mistake2 = node
            prev = node
        mistake1.val, mistake2.val = mistake2.val, mistake1.val
        
    def inorder(self, node):
        if node.left:
            yield from self.inorder(node.left)
        yield node
        if node.right:
            yield from self.inorder(node.right)
