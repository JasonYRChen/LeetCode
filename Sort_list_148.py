# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#        # Solution 1. O(nlgn) running time and O(1) space
#        if not head or not head.next:
#            return head
#
#        pivot = fast = head
#        while fast:
#            fast = fast.next
#            if fast and fast.next:
#                fast = fast.next
#                pivot = pivot.next
#        list_node1 = self.sortList(pivot.next)
#        pivot.next = None
#        list_node2 = self.sortList(head)
#
#        dummy = node = ListNode()
#        while list_node1 or list_node2:
#            if list_node1 and (not list_node2 or list_node1.val < list_node2.val):
#                node.next = list_node1
#                node, list_node1 = node.next, list_node1.next
#            else:
#                node.next = list_node2
#                node, list_node2 = node.next, list_node2.next
#        return dummy.next


        # Solution 2. O(nlgn) running time, but O(n) space, much faster than solution 1
        nums = []
        node = head
        while node:
            nums.append(node.val)
            node = node.next
        nums.sort()
        node = head
        for i in range(len(nums)):
            node.val = nums[i]
            node = node.next
        return head

