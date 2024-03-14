class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        idx_pop = 0
        for n in pushed:
            stack.append(n)
            while stack and stack[-1] == popped[idx_pop]:
                stack.pop()
                idx_pop += 1
        return idx_pop == len(popped)
