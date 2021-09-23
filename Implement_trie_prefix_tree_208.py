class Trie:
    def __init__(self):
        self.data = {}

    def insert(self, word: str) -> None:
        data = self.data
        for char in word:
            if char not in data:
                data[char] = {}
            data = data[char]
        data['.'] = '.'

    def search(self, word: str) -> bool:
        data = self.data
        for char in word:
            if char not in data:
                return False
            data = data[char]
        return '.' in data

    def startsWith(self, prefix: str) -> bool:
        data = self.data
        for char in prefix:
            if char not in data:
                return False
            data = data[char]
        return True

