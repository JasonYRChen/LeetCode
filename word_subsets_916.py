class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counter = Counter()
        for word in words2:
            counter |= Counter(word)

        words1 = deque(words1)
        for _ in range(len(words1)):
            word = words1.popleft()
            for c, value in counter.items():
                if word.count(c) < value:
                    break
            else:
                words1.append(word)
        return words1
