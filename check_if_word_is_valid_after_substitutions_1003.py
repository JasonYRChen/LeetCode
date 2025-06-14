class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == 'c':
                if not (len(stack) > 1 and stack.pop() == 'b' and stack.pop() == 'a'):
                    return False
            else:
                stack.append(c)
        return not stack
