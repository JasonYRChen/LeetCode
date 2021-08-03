# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        head = left_node = ListNode(next=head)
        
        for _ in range(left - 1):
            left_node = left_node.next
            
        last_node = left_node.next
        for _ in range(right - left):
            temp_node = last_node.next
            left_node.next, temp_node.next, last_node.next = temp_node, left_node.next, temp_node.next
        return head.next

