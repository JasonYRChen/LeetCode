from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict):
        word_dict = defaultdict(set)
        for word in wordDict:
            word_dict[len(word)].add(word)
        return [item for item in self.combinations(s, word_dict)]

    def combinations(self, s, word_dict):
        if not s:
            yield ''
        else:
            for length in word_dict:
                if s[:length] in word_dict[length]:
                    for word in self.combinations(s[length:], word_dict):
                        yield s[:length] + ' ' + word if word else s[:length]
    

#    def wordBreak(self, s: str, wordDict):
#        wordDict = set(wordDict)
#        return [item for item in self.combinations(s, wordDict)]
#
#    def combinations(self, s, word_set):
#        if not s:
#            yield ''
#        else:
#            for i in range(len(s)):
#                if s[:i+1] in word_set:
#                    for word in self.combinations(s[i+1:], word_set):
#                        yield s[:i+1] + ' ' + word if word else s[:i+1]


if __name__ == '__main__':
    s = "pineapplepenapple"
    w = ["apple","pen","applepen","pine","pineapple"]
    print(Solution().wordBreak(s, w))

