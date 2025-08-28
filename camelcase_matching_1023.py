class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        match = []
        for word in queries:
            index = 0
            for c in word:
                if index < len(pattern) and c == pattern[index]:
                    index += 1
                elif c.isupper():
                    match.append(False)
                    break
            else:
                match.append(True if index == len(pattern) else False)
        return match
