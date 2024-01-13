class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # O(n) speed, O(n) space
        s_stack = []
        for c in s:
            if c == '#' and s_stack:
                s_stack.pop()
            elif c != '#':
                s_stack.append(c)

        t_stack = []
        for c in t:
            if c == '#' and t_stack:
                t_stack.pop()
            elif c != '#':
                t_stack.append(c)
        return s_stack == t_stack
