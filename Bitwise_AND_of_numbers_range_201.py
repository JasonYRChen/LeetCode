class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift

#        # Solution 2.
#        ans, power = 0, 0
#        while left:
#            left, remainder = divmod(left, 2)
#            power += 1
#            if remainder:
#                next_num = (left + 1) * 2 ** power
#                ans += 0 if left < next_num <= right else 2 ** (power - 1)
#        return ans


if __name__ == '__main__':
    import sys

    print(Solution().rangeBitwiseAnd(int(sys.argv[1]), int(sys.argv[2])))

