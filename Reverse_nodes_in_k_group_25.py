class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        head = start = node = ListNode(next=head)
        nodes = []
        while node:
            node = node.next
            if len(nodes) < k and node is not None:
                nodes.append(node)
            elif len(nodes) == k:
                while nodes:
                    start.next = nodes.pop()
                    start = start.next
                start.next = node
                nodes = [node]
        return head.next
