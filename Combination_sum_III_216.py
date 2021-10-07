class Solution:
    def combinationSum3(self, k: int, n: int):
        return [answer for answer in self.dfs(k, n, [])]

    def dfs(self, k, n, candidate):
        last_num = candidate[-1] if candidate else 0
        if k == 1 and last_num < n <= 9:
            yield candidate + [n]
        elif k > 1 and 0 < n / k <= 9:
            start = last_num + 1
            end = start + n - ((k-1) * start + sum(i+1 for i in range(k-1)))
            while start <= end:
                yield from self.dfs(k-1, n-start, candidate+[start])
                start += 1


if __name__ == '__main__':
    import sys

    print(Solution().combinationSum3(int(sys.argv[1]), int(sys.argv[2])))
        
