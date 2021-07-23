class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x
        while start <= end:
            mid = (start + end) // 2
            square = mid**2
            if square == x:
                return mid
            if square > x:
                end = mid - 1
            else:
                start = mid + 1
                ans = mid
        return ans

