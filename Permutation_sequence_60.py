class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        result = [i+1 for i in range(n)]
        bases = [factorial(i) for i in range(n-1, -1, -1)]
        for i in range(n):
            ith = k // bases[i]
            if ith != 0:  # It doen't matter to add this line to make it work, but this can accelerate
                num = result[i+ith]
                result[i], result[i+1:i+ith+1] = num, result[i:i+ith]
                k -= ith * bases[i]
        return ''.join(str(i) for i in result)
