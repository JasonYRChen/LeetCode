class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # O(logn) time, O(1) space
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid+k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left: left + k]


        # O(k) + O(logn) time, O(1) space
#        insert, right = 0, len(arr)
#        while insert < right:
#            mid = (insert + right) // 2
#            if arr[mid] >= x:
#                right = mid
#            else:
#                insert = mid + 1

#        end = max(0, insert - k) + k
#        total_diff = sum(map(lambda n: abs(x-n), arr[end-k: end]))
#        for e in range(end, min(len(arr), insert + k)):
#            temp = total_diff - abs(x - arr[e - k]) + abs(x - arr[e])
#            if temp < total_diff:
#                end = e + 1
#                total_diff = temp
#            elif temp > total_diff:
#                break
#        return arr[end-k: end]

        # O(n) time, O(n) space
#        abs_diffs = [abs(x - n) for n in arr]
#        total = sum(abs_diffs[:k])
#        end = k
#        for i in range(k, len(arr)):
#            temp = total + abs_diffs[i] - abs_diffs[i - k]
#            if temp < total:
#                end = i + 1
#                total = temp
#            elif temp > total:
#                break
#        return arr[end - k: end]
