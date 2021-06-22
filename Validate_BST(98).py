class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.check(root)
        
    
    def check(self, node, low=float('-inf'), high=float('inf')):
        if node is None:
            return True
        if node.val >= high or node.val <= low:
            return False
        return self.check(node.left, low, node.val) and self.check(node.right, node.val, high)
