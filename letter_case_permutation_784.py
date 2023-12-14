class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def permutation(s):
            if not s:
                yield ''
            else:
                for seq in permutation(s[1:]):
                    if s[0].isdigit():
                        yield s[0] + seq
                    else:
                        yield s[0].lower() + seq
                        yield s[0].upper() + seq
        

        return [string for string in permutation(s)]
