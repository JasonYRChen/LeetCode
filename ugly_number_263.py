class Solution:
    def isUgly(self, n: int) -> bool:
        # method 1: recursion
        """
        if n == 1:
            return True
        
        if n > 1:
            n2, q2 = divmod(n, 2)
            n3, q3 = divmod(n, 3)
            n5, q5 = divmod(n, 5)
            if q2 == 0:
                return self.isUgly(n2)
            elif q3 == 0:
                return self.isUgly(n3)
            elif q5 == 0:
                return self.isUgly(n5)
        return False
        """

        # method 2. loops
        if n > 0: # this is only for speedup. Not necessary to general form
            for prime in (2, 3, 5):
                while not n % prime:
                    n //= prime
        return True if n == 1 else False
