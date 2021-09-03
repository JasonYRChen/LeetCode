# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        nums = []
        while node:
            nums.append(node.val)
            node = node.next
        nums.sort()
        node = head
        for i in range(len(nums)):
            node.val = nums[i]
            node = node.next
        return head 

