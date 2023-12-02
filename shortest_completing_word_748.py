class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        ans = None
        plate_counter = Counter([s.lower() for s in licensePlate if s.isalpha()])
        for word in words:
            for c, n in plate_counter.items():
                if word.count(c) < n:
                    break
            else:
                ans = word if ans is None or len(word) < len(ans) else ans
        return ans

        # This solution has simpler code, but may encounter lots of irrelevant charactors and waste time
#        ans = None
#        plate_counter = Counter([s.lower() for s in licensePlate if s.isalpha()])
#        for word in words:
#            if not plate_counter - Counter(word) and (ans is None or len(word) < len(ans)):
#                ans = word
#        return ans
