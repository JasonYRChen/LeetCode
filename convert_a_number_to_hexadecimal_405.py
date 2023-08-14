class Solution:
    def toHex(self, num: int) -> str:
        num_map = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        if num < 0:
            num = 2 ** 32 + num
        
        hex_string = ''
        while num:
            num, remainder = divmod(num, 16)
            if remainder in num_map:
                remainder = num_map[remainder]
            hex_string = str(remainder) + hex_string
        return hex_string if hex_string else '0'
