class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n_counter = Counter(str(n))
        upper_limit = sum(n_counter.values()) + 1
        digits = 1
        power = 0
        while digits < upper_limit:
            num = str(2 ** power)
            if (len(num) == upper_limit - 1) and not (Counter(num) - n_counter):
                return True
            power += 1
            digits = len(num)
        return False 
