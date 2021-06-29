class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = node = ListNode()
        while l1 or l2:
            if not l1 or not l2:
                node.next = l1 if l1 else l2
                return head.next
            if l1.val <= l2.val:
                node.next = l1
                node, l1 = node.next, l1.next
            else:
                node.next = l2
                node, l2 = node.next, l2.next
