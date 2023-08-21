class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
                (1+row)*row/2 <= n
            --> (1+row)*row <= 2n
            --> row**2 <= 2n
            --> row <= sqrt(2n)
        """

        row = int((2 * n)**0.5)
        while row * (row + 1) <= 2 * n:
            row += 1
        return row - 1
