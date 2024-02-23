class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leading = []
        leading_votes = 0
        counts = defaultdict(int)
        for person in persons:
            counts[person] += 1
            leading_votes = max(leading_votes, counts[person])
            latest_leading = person if counts[person] >= leading_votes else self.leading[-1]
            self.leading.append(latest_leading)

    def q(self, t: int) -> int:
        left, right = 0, len(self.leading)
        while left < right:
            mid = (left + right) // 2
            if self.times[mid] <= t:
                left = mid + 1
            else:
                right = mid
        return self.leading[left - 1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
