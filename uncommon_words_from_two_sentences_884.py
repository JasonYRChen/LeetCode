class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counter = Counter((s1 + ' ' + s2).split())
        return [k for k, c in counter.items() if c == 1]

        # solution 2
#        counter1, counter2 = Counter(s1.split()), Counter(s2.split())
#        queue = deque(counter1.keys() | counter2.keys())
#        for _ in range(len(queue)):
#            key = queue.popleft()
#            if counter1[key] + counter2[key] == 1:
#                queue.append(key)
#        return queue
