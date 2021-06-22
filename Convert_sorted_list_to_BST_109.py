# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        array = []
        while head:
            array.append(head.val)
            head = head.next
        return self.balance(array, 0, len(array))
        
    def balance(self, array, start, end):
        if start == end:
            return None
        index = (start + end) // 2
        node = TreeNode(array[index])
        node.left, node.right = self.balance(array, start, index), self.balance(array, index+1, end)
        return node
