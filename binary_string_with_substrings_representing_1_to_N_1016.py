class Solution:
    def queryString(self, s: str, n: int) -> bool:
        # self-made without using built-in method
#        s = s.lstrip('0')
#        for num in range(n, 0, -1):
#            binary = bin(num)[2:]
#            for i in range(len(s)):
#                for j in range(len(binary)):
#                    if i + j == len(s):
#                        return False
#                    if s[i+j] != binary[j]:
#                        break
#                else:
#                    break # only when binary is found
#            else:
#                return False # binary not found in s
#        return True

        for num in range(n, 0, -1):
            if bin(num)[2:] not in s:
                return False
        return True
