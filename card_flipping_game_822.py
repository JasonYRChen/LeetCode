class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        numbers = set()
        overlap = set()
        for front, back in zip(fronts, backs):
            if front == back:
                overlap.add(front)
            else:
                numbers.update([front, back])
        numbers -= overlap
        return min(numbers) if numbers else 0
