class Solution:
    def totalNQueens(self, n: int) -> int:
        array_set = [{i for i in range(n)} for _ in range(n)]
        return sum(self.sort_element(array_set, [], n))
        
        
    def sort_element(self, array_set, candidates, length):
        if not array_set or not array_set[0]:
            if len(candidates) == length:
                yield 1
        else:
            for num in array_set[0]:
                new_candidates  = candidates + [num]
                new_array_set = [e.copy() for e in array_set[1:]]
                for i, per_set in enumerate(new_array_set, 1):
                    if num in per_set:
                        per_set.remove(num)
                    if num - i in per_set:
                        per_set.remove(num - i)
                    if num + i in per_set:
                        per_set.remove(num + i)
                yield from self.sort_element(new_array_set, new_candidates, length)
