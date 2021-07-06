class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.bisect(nums, target, 0, len(nums)-1)
        
    def bisect(self, array, target, start, end):
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        if start >= end:
            return -1
        start1, start2 = (start, mid + 1) if array[start] < array[mid] else (mid + 1, start)
        end1, end2 = (mid, end) if array[start] < array[mid] else (end, mid)
        if array[start1] <= target <= array[end1]:
            return self.bisect(array, target, start1, end1)
        return self.bisect(array, target, start2, end2)
