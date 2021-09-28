class Solution:
    def findWords(self, board, words):
        prefix = {board[row][col] for row in range(len(board)) for col in range(len(board[0]))}
        words_dict = {}
        for word in words:
            if word[0] in prefix:
                data = words_dict
                for char in word:
                    if char in data:
                        data = data[char]
                        data['count'] += 1
                    else:
                        data[char] = {}
                        data = data[char]
                        data['count'] = 1

        remain_words = set(words)
        ans = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                found = self.dfs(board, row, col, '', set(), words_dict, set(), remain_words)
                if found:
                    ans.extend(found)
                    for word in found:
                        data = words_dict
                        for char in word:
                            data[char]['count'] -= 1
                            data = data[char]
        return ans

    def dfs(self, board, row, col, word, found, words_dict, visited, remain_words):
        char = board[row][col]
        word = word + char
        if word in remain_words:
            remain_words.remove(word)
            found.add(word)
        if char in words_dict and words_dict[char]['count']:
            visited = visited | {(row, col)}
            candidates = {(row+i, col+j) for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1))
                          if 0 <= row + i < len(board) and 0 <= col + j < len(board[0])}
            candidates -= visited
            for row, col in candidates:
                self.dfs(board, row, col, word, found, words_dict[char], visited, remain_words)
        return found


if __name__ == '__main__':
    b = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    w = ["oath","pea","eat","rain","oathi","oathk","oathf","oate","oathii","oathfi","oathfii"]
    print(Solution().findWords(b, w))

