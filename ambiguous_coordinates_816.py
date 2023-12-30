class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def valid_number(s):
            if len(s) == 1:
                yield s
            elif s.startswith('0') and not s.endswith('0'):
                yield '0.' + s[1:]
            elif not s.startswith('0'):
                yield s
                if not s.endswith('0'):
                    for i in range(1, len(s)):
                        yield s[:i] + '.' + s[i:]


        answer = []
        for i in range(2, len(s) - 1):
            for left in valid_number(s[1:i]):
                for right in valid_number(s[i:len(s) - 1]):
                    answer.append(f'({left}, {right})')
        return answer
