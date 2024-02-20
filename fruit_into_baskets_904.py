class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        last_index = {}
        total, max_total = 0, 0
        for i in range(len(fruits)):
            if fruits[i] not in last_index and len(last_index) == 2:
                index = (last_index.keys() - {fruits[i], fruits[i-1]}).pop()
                total = i - last_index.pop(index) - 1
            last_index[fruits[i]] = i
            total += 1
            max_total = max(max_total, total)
        return max_total
