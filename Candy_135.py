class Solution:
    def candy(self, ratings) -> int:
        number = len(ratings)
        dp = [1] * number
        for step in range(1, number):
            if ratings[step] > ratings[step-1]:
                dp[step] = max(dp[step], dp[step-1]+1)
            if ratings[number-1-step] > ratings[number-step]:
                dp[number-1-step] = max(dp[number-1-step], dp[number-step]+1)
        return sum(dp)


#        dp = [1] * len(ratings)
#        for index in range(1, len(ratings)):
#            if ratings[index] > ratings[index-1]:
#                dp[index] = dp[index-1] + 1
#        for index in range(len(ratings)-2, -1, -1):
#            if ratings[index] > ratings[index+1]:
#                dp[index] = max(dp[index], dp[index+1] + 1)
#        return sum(dp)


if __name__ == '__main__':
    r = [1, 0, 2]
    print(Solution().candy(r))

