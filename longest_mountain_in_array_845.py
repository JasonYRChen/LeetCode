class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        # one pass, O(n) time, O(1) space
        rising = True
        max_length, length = 0, 1
        for i in range(1, len(arr)):
            if not arr[i] == arr[i-1]:
                if rising and i > 1 and arr[i] < arr[i-1] and arr[i-1] > arr[i-2]:
                    rising = False
                elif rising and arr[i] < arr[i-1]:
                    length = 0
                elif not rising and arr[i] > arr[i-1]:
                    rising = True
                    max_length = max(max_length, length)
                    length = 1
                length += 1
            else:
                if not rising:
                    max_length = max(max_length, length)
                    rising = True
                length = 1
        return max(max_length, length if length > 2 and not rising else 0)
