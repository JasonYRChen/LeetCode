class Solution:
    def digit_sort(self, arr, index):
        if index == 3:
            return 3

        max_digit = 9
        if index == 0:
            max_digit = 2
        elif index == 1 and arr[0] == 2:
            max_digit = 3
        elif index == 2:
            max_digit = 5
        
        final_index = index
        for i in range(max_digit, -1, -1):
            try:
                new_idx = arr[index:].index(i) + index
            except:
                continue

            arr[index], arr[new_idx] = arr[new_idx], arr[index]
            final_index = self.digit_sort(arr, index+1)
            if final_index == 3:
                break

        return final_index

    def largestTimeFromDigits(self, arr: List[int]) -> str:
        final_index = self.digit_sort(arr, 0)
        return f'{arr[0]}{arr[1]}:{arr[2]}{arr[3]}' if final_index == 3 else ''
