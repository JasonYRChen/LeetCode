# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0
        node = head
        while node:
            count += 1
            node = node.next
        number, remain = divmod(count, k)
        partition = []
        while head:
            i = 0
            partition.append(head)
            while i < number + (1 if remain else 0):
                i += 1
                prev, head = head, head.next
            prev.next = None
            remain -= 1 if remain else 0
        partition.extend([None] * (k - count))
        return partition
