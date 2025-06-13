class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter = Counter(words[0])
        for word in words[1:]:
            counter &= Counter(word)
        
        output = [s for s in counter.keys() for _ in range(counter[s])]
        return output
