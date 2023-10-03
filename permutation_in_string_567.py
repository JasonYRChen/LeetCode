class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        keys = set(counter.keys())
        exhausted = set()
        temp = Counter()
        numbers = 0
        for i, c in enumerate(s2):
            if c in counter:
                if counter[c]:
                    temp[c] += 1
                    counter[c] -= 1
                    numbers += 1
                    if not counter[c]:
                        exhausted.add(c)
                        if exhausted == keys:
                            return True
                else:
                    while s2[i-numbers] != c:
                        temp[s2[i-numbers]] -= 1
                        counter[s2[i-numbers]] += 1
                        exhausted.discard(s2[i-numbers])
                        numbers -= 1
            else:
                counter += temp
                exhausted = set()
                temp = Counter()
                numbers = 0
        return False
