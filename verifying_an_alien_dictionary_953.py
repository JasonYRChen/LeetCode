class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = {c: i for i, c in enumerate(order)}
        order[None] = -1

        for i in range(1, len(words)):
            for c1, c2 in zip_longest(words[i-1], words[i]):
                if order[c1] < order[c2]:
                    break
                if order[c1] > order[c2]:
                    return False
        return True
