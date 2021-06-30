class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Version 1: use heap
        # h = [(n.val, i, n) for i, n in enumerate(lists) if n]
        # heapify(h)
        # head = node = ListNode()
        # while h:
        #     _, i, n = heappop(h)
        #     node.next = n
        #     if n.next:
        #         heappush(h, (n.next.val, i, n.next))
        #     node = n
        # return head.next
        
        # Version 2: crack all the nodes and sort them
        nodes = []
        for node in lists:
            while node:
                nodes.append(node)
                node = node.next
        
        nodes.sort(key=lambda x: x.val)
        head = n = ListNode()
        for node in nodes:
            n.next = node
            n = n.next
        return head.next
