# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
            This is actually implementing binary search, since 'n'
            implicitly refers to a sorted list from 1 to n.
        """

        start, end = 1, n
        while end >= start:
            mid = (end + start) // 2
            if isBadVersion(mid):
                end = mid - 1
            else:
                start = mid + 1
        return start
