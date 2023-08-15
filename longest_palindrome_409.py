class Solution:
    def longestPalindrome(self, s: str) -> int:
        # solution 1: time O(n)
        counter = defaultdict(int)
        length = 0
        for c in s:
            counter[c] += 1
            if counter[c] == 2:
                length += 2
                del counter[c]
        return length + 1 if counter else length

        # solution 2: time 2*O(n)
        """
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1
        
        has_odd = False
        length = 0
        for num in counter.values():
            div, mod = divmod(num, 2)
            length += div * 2
            if mod:
                has_odd = True
        return length + 1 if has_odd else length
        """
