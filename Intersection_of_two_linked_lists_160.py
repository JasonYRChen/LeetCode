# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # Solution 1. O(m+n) running time, O(1) space
        node_a, node_b = headA, headB
        while node_a != node_b:
            node_a = node_a.next if node_a else headB
            node_b = node_b.next if node_b else headA
        return node_a        


#        # Solution 2. O(m+n) running time, O(m+n) space
#        nodes = set()
#        while headA:
#            nodes.add(headA)
#            headA = headA.next
#        
#        while headB:
#            if headB in nodes:
#                return headB
#            headB = headB.next
#        return None      

