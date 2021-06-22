class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        for i in range(n):
            array_set = [{num for num in range(n)} for _ in range(n)]
        
        for combination in self.sort_element(array_set, [], n):
            sub_ans = []
            for idx in combination:
                string = ['.'] * n
                string[idx] = 'Q'
                string = ''.join(string)
                sub_ans.append(string)
            ans.append(sub_ans)
        return ans
            
            
    def sort_element(self, array_set, candidates, length):
        if not array_set or not array_set[0]:
            if len(candidates) == length:
                yield candidates
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


