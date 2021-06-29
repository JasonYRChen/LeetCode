class Solution:
    def isValid(self, s: str) -> bool:
        p_dict = {')': '(', '}': '{', ']': '['}
        bucket = []
        for p in s:
            if p in p_dict.values():
                bucket.append(p)
            else:
                if not bucket or bucket.pop() != p_dict[p]:
                    return False
        return bucket == []
