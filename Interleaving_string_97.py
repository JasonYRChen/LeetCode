class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        stack, used = [(0, 0)], {(0, 0)}
        while stack:  # need to verify afterward
            index1, index2 = stack.pop()
            if index1 + index2 == len(s3):
                return True
            
            if index1 < len(s1) and s1[index1] == s3[index1 + index2] and (index1+1, index2) not in used:
                stack.append((index1+1, index2))
                used.add((index1+1, index2))
            if index2 < len(s2) and s2[index2] == s3[index1 + index2] and (index1, index2+1) not in used:
                stack.append((index1, index2+1))
                used.add((index1, index2+1))
        return False

