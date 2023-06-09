from collections import defaultdict
from itertools import zip_longest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
            zip_longest return 'None' if any iterable inside of it exhausted.
            Collecting 'None' inside of defaultdict avoids redundant length
            check of 's' and 't'. This may not be efficient in case of length 
            inequality, but it offers a general and consistent solution.
        """

        counter = defaultdict(int)
        for a, b in zip_longest(s, t):
            counter[a] += 1
            counter[b] -= 1
        if None not in counter and not any(counter.values()):
            return True
        return False
