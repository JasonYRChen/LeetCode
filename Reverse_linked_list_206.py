# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        head, node = ListNode(next=head), head
        while node and node.next:
            insert_node = node.next
            node.next, head.next, insert_node.next = insert_node.next, insert_node, head.next
        return head.next

