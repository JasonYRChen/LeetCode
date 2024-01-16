class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = defaultdict(int)
        for i in hand:
            counter[i] += 1
        
        queue = deque(sorted(counter.keys()))
        while queue:
            start = queue[0]
            for i in range(groupSize):
                if start + i not in counter or not counter[start+i]:
                    return False
                counter[start+i] -= 1
            while queue and not counter[queue[0]]:
                queue.popleft()
        return True
