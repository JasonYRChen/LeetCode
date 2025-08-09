# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        indices = []
        result = []
        index = 0
        while head:
            while indices and head.val > result[indices[-1]]:
                result[indices[-1]] = head.val
                indices.pop()
            indices.append(index)
            result.append(head.val)
            index += 1
            head = head.next
        
        for i in indices:
            result[i] = 0
        return result
