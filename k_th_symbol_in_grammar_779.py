class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        """
            (This is a O(ln n) running time and O(ln n) space process)
            Imagine using a tree to store each row's composition, like
                                       0
                                      / \
                                     0   1
                                    / \ / \
                                   0  1 1  0
                                   ...
            We use a two-stages process to find the answer. The first bottom-up stage is to find
            the relative position of child to its parent in each row. Take (n, k) = (3, 3) element
            for example, it is a '1' on the left of its parent '1', and its parent '1' is on the
            right of its grandparent. We record the 'left'(use 0 to represent) and 'right' (use 1
            to represent) along way to the top.
            The upcoming stage 2 is a top-down process following the relative positions to find 
            the final element. Starting from the pool [0, 1] and choose the element according to 
            the first relative positions. If the first one is 1, then in next round we choose the 
            next element from a new pool [1, 0], otherwise remain the same pool.
        """

        # stage 1: record relative position
        path = [] # save 1 for right, 0 for left
        for _ in range(n - 1):
            path.append((k + 1) % 2)
            k = k // 2 + k % 2

        # stage 2: find final element
        num = 0 
        pool = [0, 1]
        for direction in path[::-1]:
            num = pool[direction]
            pool = [1, 0] if num else [0, 1]
        return num
