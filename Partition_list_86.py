# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        head = ListNode(None, head)
        insert_node = node = head
        while node:
            if node.next and node.next.val < x:
                to_insert_node = node.next
                node.next = node.next.next
                insert_node.next, to_insert_node.next = to_insert_node, insert_node.next
                insert_node = insert_node.next
            if node.next == insert_node or not node.next or node.next.val >= x:
                node = node.next
        return head.next
    
#     # Solution 2: using list to do partition. Space consuming, but still O(n) running time.
#     def partition(self, head: ListNode, x: int) -> ListNode:
#         p_small, p_large, node = [], [], head

#         while node:
#             if node.val < x:
#                 p_small.append(node.val)
#             else:
#                 p_large.append(node.val)
#             node = node.next
#         vals = p_small + p_large
        
#         node = head
#         for val in vals:
#             node.val = val
#             node = node.next

#         return head

