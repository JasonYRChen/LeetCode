class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for c in s:
            if not stack or not (stack[-1] == '(' and c == ')'):
                stack.append(c)
            else:
                stack.pop()
        return len(stack)
