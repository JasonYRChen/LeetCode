class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # w/o modifying string
#        stack = []
#        to_delete = set()
#        for i, p in enumerate(s):
#            if p == ')' and len(stack) == 1:
#                to_delete |= {stack.pop(), i}
#            elif p == ')':
#                stack.pop()
#            else:
#                stack.append(i)
#        s_list = [c for i, c in enumerate(s) if i not in to_delete]
#        return ''.join(s_list)

        # directly modify string
        leading_p = 0
        current_p = -1
        new_s = ''
        for i in range(len(s)):
            if s[i] == ')':
                if current_p == leading_p:
                    new_s += s[leading_p+1: i]
                    leading_p = i + 1
                    current_p = i
                else:
                    current_p -= 1
            else:
                current_p += 1
        return new_s
