class Solution:
    def calPoints(self, operations: List[str]) -> int:
        end = 0
        for token in operations:
            if token not in {'C', 'D', '+'}:
                operations[end] = int(token)
            elif token == 'D':
                operations[end] = 2 * operations[end - 1]
            elif token == '+':
                operations[end] = operations[end - 1] + operations[end - 2]
            end += -1 if token == 'C' else 1
        return sum(operations[:end])
