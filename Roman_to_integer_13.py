class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        for i in range(len(s)):
            is_single = i+1 == len(s) or (i+1 < len(s) and roman[s[i]] >= roman[s[i+1]])
            num += roman[s[i]] if is_single else -roman[s[i]]
        return num
        
        # roman_dict = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 
        #               'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        # num, index = 0, 0
        # while index < len(s):
        #     if roman_dict.get(s[index:index+2]):
        #         num += roman_dict[s[index:index+2]]
        #         index += 2
        #     else:
        #         num += roman_dict[s[index]]
        #         index += 1
        # return num
        
