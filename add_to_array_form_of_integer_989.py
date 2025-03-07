class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ans = []
        digit = 0
        while digit or num or k:
            k, r = divmod(k, 10)
            n = num.pop() if num else 0
            digit, n_append = divmod(r + n + digit, 10)
            ans.append(n_append)
            
        return ans[::-1]
