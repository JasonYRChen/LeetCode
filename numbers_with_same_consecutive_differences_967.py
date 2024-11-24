class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        integers = []
        denominator = 10 ** (n - 1)
        for i in range(1, 10):
            temp = [i]
            while temp:
                num = temp.pop()
                if num // denominator:
                    integers.append(num)
                else:
                    last_digit = num % 10
                    if last_digit + k < 10:
                        temp.append(num * 10 + last_digit + k)
                    if (last_digit - k >= 0) and k != 0:
                        temp.append(num * 10 + last_digit - k)
        return integers
