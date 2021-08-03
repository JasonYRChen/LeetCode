class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        return list(self.valid_address(s, 1))
        
    def valid_address(self, s, times):
        if s and len(s) <= (4 - times + 1) * 3:
            if times == 4 and (s[0] != '0' or s == '0') and int(s) <= 255:
                yield s
            else:
                for end in range(1, min(3, len(s)-1) + 1):
                    num = s[:end]
                    if num == '0' or (num[0] != '0' and int(num) <= 255):
                        for address in self.valid_address(s[end:], times+1):
                            yield s[:end] + '.' + address

