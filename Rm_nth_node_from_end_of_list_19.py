class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nth, node, prev = head, head, None
        ith = 1
        while node.next:
            node = node.next
            if ith < n:
                ith += 1
            else:
                nth, prev = nth.next, nth
        if prev is None:
            return head.next
        prev.next = nth.next
        return head
