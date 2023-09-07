class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1, r2, r3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        result = []
        for word in words:
            w = set(word.lower())
            not_in_one_row = (w - r1) and (w - r2) and (w - r3)
            if not not_in_one_row:
                result.append(word)
        return result
