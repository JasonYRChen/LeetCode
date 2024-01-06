class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        work_price = {}
        for d, p in zip(difficulty, profit):
            if d not in work_price:
                work_price[d] = p
            else:
                work_price[d] = max(work_price[d], p)
                
        difficulty.sort()
        best_profit = [0 for _ in range(len(profit) + 1)]
        for i in range(len(profit)):
            best_profit[i+1] = max(best_profit[i], work_price[difficulty[i]])

        earned = 0
        for man in worker:
            index = bisect_right(difficulty, man)
            earned += best_profit[index]
        return earned
