class Solution:
    def reverseBits(self, n: int) -> int:
        num_string = bin(n)[2:]
        num_string = '0' * (32 - len(num_string)) + num_string
        return int(num_string[::-1], 2)

