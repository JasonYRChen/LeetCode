# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp, head = 0, ListNode()
        node = head
        while l1 or l2 or temp:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            next_node = ListNode((n1 + n2 + temp) % 10)
            temp = (n1 + n2 + temp) // 10
            node.next, node = next_node, next_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next

