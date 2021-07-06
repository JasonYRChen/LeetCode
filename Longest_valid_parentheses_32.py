class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_val = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_val = max(max_val, i-stack[-1])
        return max_val

        # counter = [0] * (len(s) + 1)
        # max_val = 0
        # for i, c in enumerate(s):
        #     if c == ')':
        #         prev = i - 1
        #         temp_count = 0
        #         while prev >= 0:
        #             if s[prev] == '(' and not counter[i+1]:
        #                 counter[i+1] = 2 + temp_count
        #                 temp_count = 0
        #                 prev -= 1
        #             if counter[prev+1]:
        #                 temp_count += counter[prev+1]
        #                 prev -= counter[prev+1]
        #             else:
        #                 break
        #         if counter[i+1]:
        #             counter[i+1] += temp_count
        #     max_val = max(max_val, counter[i+1])
        # return max_val
        
