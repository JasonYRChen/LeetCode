class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # Solution 1: This is a stricted ascending or descending mountain, no worry about the flat case
        left, right = 0, len(arr)
        while True:
            mid = (left + right) // 2
            if arr[mid] > max(arr[mid-1], arr[mid+1]):
                return mid
            if arr[mid] > arr[mid-1]:
                left = mid
            else:
                right = mid

        # Solution 2: This is for on the left or right of the peak there exists a flat
#        left, right = 0, len(arr)
#        while True:
#            mid = (left + right) // 2
#            if arr[mid] > max(arr[mid-1], arr[mid+1]):
#                return mid
#            if arr[mid] > arr[mid-1]:
#                left = mid
#            elif arr[mid] < arr[mid-1]:
#                right = mid
#            else:
#                i = 0
#                while mid + i < len(arr) and arr[mid+i] == arr[mid]:
#                    i += 1
#                if mid + i < len(arr) and arr[mid+i] > arr[mid]:
#                    left = mid + i - 1
#                else:
#                    i = 0
#                    while arr[mid-i] == arr[mid]:
#                        i += 1
#                    right = mid - i + 1
