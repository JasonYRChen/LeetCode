class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        left, right = 0, len(arr) - 1
        while left + 1 < len(arr) and arr[left+1] > arr[left]:
            left += 1
        while right - 1 > -1 and arr[right-1] > arr[right]:
            right -= 1
        return True if left == right and left != 0 and left != len(arr) - 1 else False
