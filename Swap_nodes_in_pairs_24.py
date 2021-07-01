class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        head = ListNode(next=head)
        node = head       
        while node.next and node.next.next:
            n1, n2 = node.next.next, node.next
            n1.next, n2.next, node.next = n2, n1.next, n1
            node = n2
        return head.next
