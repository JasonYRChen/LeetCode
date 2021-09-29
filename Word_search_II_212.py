class Solution:
    def findWords(self, board, words):
        words_dict = {}
        for word in words:
            data = words_dict
            for char in word[::-1]:
                if char not in data:
                    data[char] = {}
                data = data[char]
            data['.'] = word

        ans = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                found = self.dfs(board, row, col, ans, words_dict, set())
        return ans 

    def dfs(self, board, row, col, ans, words_dict, visited):
        char = board[row][col]
        if char in words_dict:
            if '.' in words_dict[char]:
                ans.append(words_dict[char]['.'])
                words_dict[char].pop('.')

            visited = visited | {(row, col)}
            candidates = {(row+i, col+j) for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1))
                          if 0 <= row + i < len(board) and 0 <= col + j < len(board[0])}
            candidates -= visited
            for row, col in candidates:
                self.dfs(board, row, col, ans, words_dict[char], visited)
            if not words_dict[char]:
                words_dict.pop(char)
            return ans 
