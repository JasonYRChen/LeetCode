class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Solution 1. Running time: O(n), space: O(n)
        visited = {}
        for index, num in enumerate(numbers, 1):
            if target - num in visited:
                return [visited[target-num], index]
            visited[num] = index

#        # Solution 2. Running time: O(nlgn), space: O(1)
#        for start in range(len(numbers)):
#            new_target = target - numbers[start]
#            left, right = start + 1, len(numbers) - 1
#            while left <= right:
#                mid = (left + right) // 2
#                if numbers[mid] == new_target:
#                    return [start + 1, mid + 1]
#                if numbers[mid] < new_target:
#                    left = mid + 1
#                else:
#                    right = mid - 1

