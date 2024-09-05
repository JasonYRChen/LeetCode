class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left, right = 0, len(tokens) - 1
        max_score, curr_score = 0, 0
        
        while left <= right:
            if power < tokens[left] and curr_score > 0:
                curr_score -= 1
                power += tokens[right]
                right -= 1

            if power >= tokens[left]:
                curr_score += 1
                power -= tokens[left]
                max_score = max(max_score, curr_score)

            left += 1

        return max_score
