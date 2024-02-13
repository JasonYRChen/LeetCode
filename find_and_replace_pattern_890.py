class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        words = deque(words)
        for _ in range(len(words)):
            mapping = {}
            found = set()
            word = words.popleft()
            for c_word, c_pattern in zip(word, pattern):
                if c_pattern not in mapping and c_word not in found:
                    mapping[c_pattern] = c_word
                    found.add(c_word)
                elif c_pattern not in mapping or mapping[c_pattern] != c_word:
                    break
            else:
                words.append(word)
        return words
