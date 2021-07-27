class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        A case like this:
           c
        1111171
        1711111
        The first, last, and middle are all 1s, there's no way to determine the partition
        that 7 belongs to by bisection method.
        """
        return target in nums

