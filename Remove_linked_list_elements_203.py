# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head, val: int):
        head = node = ListNode(next=head)
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return head.next
