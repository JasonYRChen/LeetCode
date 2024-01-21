class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        lapses = {p: (target-p)/s for p, s in zip(position, speed)}
        fleets = 0
        lapse = 0
        for p in sorted(lapses.keys(), reverse=True):
            if lapses[p] > lapse:
                lapse = lapses[p]
                fleets += 1
        return fleets
