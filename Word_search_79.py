class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        c_board, chars = defaultdict(int), defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board[0])):
                chars[board[row][col]].add((row, col))
                c_board[board[row][col]] += 1
        
        for c in word:
            c_board[c] -= 1
            if c_board[c] < 0:
                return False
        return self.guess(word, chars, set())
        
    def guess(self, word, chars, used, index=0, row=0, col=0):
        if index == len(word):
            return True if index == len(used) else False
        
        candidates = ({(row-1, col), (row+1, col), (row, col-1), (row, col+1)} - used) & chars[word[index]] \
                        if index else chars[word[0]]
            
        for row, col in candidates:
            used.add((row, col))
            if self.guess(word, chars, used, index+1, row, col):
                return True
            used.remove((row, col))
        return False
        
