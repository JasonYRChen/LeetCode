# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return

        pivot = fast = head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                pivot = pivot.next

        dummy = ListNode(next=pivot.next)
        pivot.next = None
        node = dummy.next
        while node and node.next:
            node_next = node.next
            node.next, node_next.next, dummy.next = node_next.next, dummy.next, node_next

        node_forward, node_backward = head, dummy.next
        while node_backward:
            next_forward = node_forward.next
            node_forward.next, node_backward.next, node_backward = node_backward, next_forward, node_backward.next
            node_forward = next_forward
     
