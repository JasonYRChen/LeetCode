class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = sorted(score, reverse=True)
        ranks_map = {}
        for i, num in enumerate(ranks, 1):
            if i == 1:
                ranks_map[num] = 'Gold Medal'
            elif i == 2:
                ranks_map[num] = 'Silver Medal'
            elif i == 3:
                ranks_map[num] = 'Bronze Medal'
            else:
                ranks_map[num] = f'{i}'
        return [ranks_map[n] for n in score]
