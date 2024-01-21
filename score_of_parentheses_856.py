class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                total = 0
                while stack[-1]:
                    total += stack.pop()
                stack.pop()
                stack.append(total * 2 if total else 1)
        return sum(stack)
