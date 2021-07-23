class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up, down = 0, len(matrix) - 1
        while up <= down:
            mid = (up + down) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                down = mid - 1
            else:
                up = mid + 1
        
        row = up - 1
        left, right = 0, len(matrix[row]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

