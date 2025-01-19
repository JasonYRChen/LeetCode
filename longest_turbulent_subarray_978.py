class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_len = 1
        temp_len = 2
        prev_num = arr[0]
        for i in range(len(arr) - 1):
            if (prev_num < arr[i] > arr[i+1]) or (prev_num > arr[i] < arr[i+1]):
                temp_len += 1
            else:
                temp_len = 2 if arr[i+1] != arr[i] else 1
            prev_num = arr[i]
            max_len = max(max_len, temp_len)
            
        return max_len
