class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return list(self.generate(n, n))

    def generate(self, left, right):
        if left == 0:
            yield ')' * right
        else:
            for left_1 in self.generate(left-1, right):
                yield '(' + left_1
            if left < right:
                for right_1 in self.generate(left, right-1):
                    yield ')' + right_1
            
