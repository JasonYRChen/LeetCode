class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = defaultdict(int)
        for c in t:
            counter[c] += 1
        
        total = 0
        left = right = None
        indices = deque()
        for i, c in enumerate(s):
            if c in counter:
                indices.append(i)
                counter[c] -= 1
                if counter[c] >= 0:
                    total += 1
                while total == len(t):
                    while counter[s[indices[0]]] < 0:
                        counter[s[indices[0]]] += 1
                        indices.popleft()
                    head = indices.popleft()
                    if left is None or i - head < right - left:
                        left, right = head, i
                    counter[s[head]] += 1
                    if counter[s[head]] > 0:
                        total -= 1
        return s[left:right+1] if left is not None else ''
