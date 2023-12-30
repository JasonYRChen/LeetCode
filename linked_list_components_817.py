# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        count = 0
        nums = set(nums)
        while head:
            if head.val in nums and (not head.next or head.next.val not in nums):
                count += 1
            head = head.next
        return count



#        count = 0
#        connected = 0
#        nums = set(nums)
#        while head:
#            if head.val in nums:
#                count += 1
#            elif count:
#                connected += 1
#                count = 0
#            head = head.next
#        return connected + 1 if count else connected
