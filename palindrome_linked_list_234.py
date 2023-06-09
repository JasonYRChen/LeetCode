# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # solution 1: brutally list all elements and compare
#    def isPalindrome(self, head) -> bool:
#        values = []
#        while head:
#            values.append(head.val)
#            head = head.next
#        return values == values[::-1]

    # solution 2: using fast and slow nodes to reach O(1) in space
    def isPalindrome(self, head) -> bool:
        """
            Palindrome comparison needs to cut list in half and compare
            the two lists elements, one go forward the other go backward.
            The 'fast and slow nodes' idea reflects the fact that cut the
            list into half: the fast node always go 2X speed than slow one.
            Before the slow node, all the previous nodes are connected
            backward, which can then be used in second phase: compare the
            two lists along different traverse directions.
        """

        fast, slow, reverse = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            temp = reverse
            reverse = slow
            slow = slow.next
            reverse.next = temp
        if fast:
            slow = slow.next

        while slow:
            if slow.val != reverse.val:
                return False
            slow = slow.next
            reverse = reverse.next
        return True


class Node:
    def __init__(self, value, n):
        self.val = value
        self.next = n

    def __str__(self):
        return f"{self.val}"


def make_nodes(array):
    head = None
    array = array[::-1]
    for i in array:
        temp = Node(i, head)
        head = temp
    return head


def show_nodes(head):
    array = []
    while head:
         array.append(head.val)
         head = head.next
    return array


array = [1, 2, 2, 1]
head = make_nodes(array)
print(Solution().isPalindrome(head))
