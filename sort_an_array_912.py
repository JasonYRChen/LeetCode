class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        return [heapq.heappop(nums) for _ in range(len(nums))]

        # solution 2.
#        numbers = defaultdict(int)
#        for num in nums:
#            numbers[num] += 1
#        keys = list(numbers.keys())

#        queue = [(0, len(keys) - 1)]
#        while queue:
#            start, end = queue.pop()
#            index = random.randint(start, end)
#            keys[index], keys[end] = keys[end], keys[index]
#            left, right = start, end - 1
#            while left <= right:
#                while left <= right and keys[left] <= keys[end]:
#                    left += 1
#                while left <= right and keys[right] > keys[end]:
#                    right -= 1
#                if left < right:
#                    keys[left], keys[right] = keys[right], keys[left]
#                    left += 1
#                    right -= 1
#            keys[left], keys[end] = keys[end], keys[left]
#            if left - start > 1:
#                queue.append((start, left - 1))
#            if end - left > 1:
#                queue.append((left + 1, end))

#        ans = []
#        for num in keys:
#            for _ in range(numbers[num]):
#                ans.append(num)

#        return ans
