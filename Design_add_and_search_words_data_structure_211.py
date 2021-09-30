from collections import defaultdict


class WordDictionary:
    def __init__(self):
        self.data = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.data[len(word)].add(word)

    def search(self, word: str) -> bool:
        for compare in self.data[len(word)]:
            for c, w in zip(compare, word):
                if w != '.' and w != c:
                    break
            else:
                return True
        return False


# A dfs solution
class WordDictionary:
    def __init__(self):
        self.data = {}

    def addWord(self, word: str) -> None:
        word = word[::-1]
        data = self.data
        for char in word:
            if char not in data:
                data[char] = {}
            data = data[char]
        data['#'] = '#'

    def search(self, word: str) -> bool:
        return self.dfs(self.data, word[::-1])

    def dfs(self, data, word):
        if not word:
            return True if '#' in data else False
        char = word[0]
        if char != '.' and char not in data:
            return False

        if char != '.':
            return self.dfs(data[char], word[1:])
        for key in data:
            if key != '#' and self.dfs(data[key], word[1:]):
                return True
        return False

