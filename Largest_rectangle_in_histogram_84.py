class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        indices = [-1]
        heights.append(0)
        area = 0
        for i in range(len(heights)):
            while heights[i] < heights[indices[-1]]:
                height = heights[indices.pop()]
                width = i - indices[-1] - 1
                area = max(area, height * width)
            indices.append(i)
        return area

