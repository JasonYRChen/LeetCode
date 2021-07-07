class Solution:
    def countAndSay(self, n: int) -> str:        
        result = '1'
        for _ in range(1, n):
            i, temp = 0, ''
            while i < len(result):
                count = 1
                while i+count < len(result) and result[i+count] == result[i]:
                    count += 1
                temp += str(count) + result[i]
                i += count
            result = temp
        return result
