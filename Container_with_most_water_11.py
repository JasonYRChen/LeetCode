class Solution:
    def maxArea(self, height):
        area, left, right = 0, 0, len(height) - 1
        while right > left:
            min_height = min(height[left], height[right])
            area = max(area, min_height * (right - left))
            while right > left and height[right] <= min_height:
                right -= 1
            while right > left and height[left] <= min_height:
                left += 1
        return area
