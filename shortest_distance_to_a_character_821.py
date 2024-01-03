class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # solution 1. O(n) time, O(1) space
        c_index = -len(s)
        answer = [0 for _ in range(len(s))]
        # forward
        for i in range(len(s)):
            if s[i] == c:
                c_index = i
            answer[i] = i - c_index
        # backward
        for i in range(len(s)-1, -1, -1):
            if s[i] == c:
                c_index = i
            answer[i] = min(answer[i], abs(i - c_index))
        return answer


        # solution 2. O(n) time, O(n) space
#        c_indices = [i for i in range(len(s)) if s[i] == c]
#        c_indices = [-len(s)] + c_indices + [2*len(s)]
#        c_index = 1

#        answer = [0 for _ in range(len(s))]
#        for i in range(len(s)):
#            if i == c_indices[c_index]:
#                c_index += 1
#            answer[i] = min(c_indices[c_index] - i, i - c_indices[c_index-1])
#        return answer
