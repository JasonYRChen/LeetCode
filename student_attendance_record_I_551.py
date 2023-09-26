class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        late = 0
        for c in s:
            if c == 'L':
                late += 1
            else:
                late = 0
                if c == 'A':
                    absent += 1
            if late == 3 or absent == 2:
                return False
        return True
