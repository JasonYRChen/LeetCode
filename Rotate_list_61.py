# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # Solution 1: Running time: O(2n), space: O(1)
        if not head:
            return head
        
        new_end = end = head
        k_temp, length = k, 1
        while k > 0 or end.next:
            if k > 0 and not end.next:
                k = length - k_temp % length - 1
                while k > 0:
                    new_end = new_end.next
                    k -= 1
            else:
                if k == 0:
                    new_end = new_end.next
                else:
                    k -= 1
                end = end.next
                length += 1
        new_head = new_end.next if new_end.next else head
        new_end.next = None
        end.next = head if end != new_end else None
        return new_head
        
        ## Solution 2: with list fully expanding the ListNode. Time: O(2n), Space: O(n)
        # if not head:
        #     return head
        # array = []
        # node = head
        # while node:
        #     array.append(node.val)
        #     node = node.next
        # start = len(array) - k % len(array)
        # node = head
        # for i in range(start, start+len(array)):
        #     node.val = array[i % len(array)]
        #     node = node.next
        # return head

