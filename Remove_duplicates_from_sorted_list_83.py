# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        head = ListNode(None, head)
        slow, fast = head, head.next
        while fast:
            next_val = fast.next.val if fast.next else None
            if fast.val != next_val:
                slow.next = fast
                slow = fast
            fast = fast.next
        return head.next

