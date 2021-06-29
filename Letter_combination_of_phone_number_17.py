class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', 
                   '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        return list(self.letters(digits, num_map, 0)) if digits else ''
        
    def letters(self, digits, num_map, index):
        if index == len(digits) - 1:
            for char in num_map[digits[-1]]:
                yield char
        else:
            for char1 in num_map[digits[index]]:
                for char3 in self.letters(digits, num_map, index+1):
                    yield char1 + char3
