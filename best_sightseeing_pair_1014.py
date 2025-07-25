class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = values[0]
        current_score = values[0]
        for v in values[1:]:
            current_score -= 1
            max_score = max(max_score, current_score + v)
            current_score = max(current_score, v)
        return max_score
