class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        execution = [0 for _ in range(n)]
        lapse = 0
        for instruction in logs:
            func, status, time = instruction.split(':')
            func, time = int(func), int(time)
            if status == 'start':
                if stack:
                    execution[stack[-1]] += time - lapse
                stack.append(func)
                execution[stack[-1]] += 1
            else:
                execution[stack.pop()] += time - lapse + 1
            lapse = time + 1
        return execution
