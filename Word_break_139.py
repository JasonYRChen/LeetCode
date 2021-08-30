class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        wordDict = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for end in range(1, len(s) + 1):
            for cut in range(end):
                if dp[cut] and s[cut:end] in wordDict:
                    dp[end] = True
                    break
        return dp[-1]


if __name__ == '__main__':
    s = "catsandog"
    d = ["cats","dog","sand","and","cat"]
    print(Solution().wordBreak(s, d))

