class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        remain = defaultdict(int)
        for bill in bills:
            remain[bill] += 1
            bill -= 5
            if bill:
                if bill == 15 and remain[10]:
                    remain[10] -= 1
                    bill -= 10
                fives = bill // 5
                if fives > remain[5]:
                    return False
                remain[5] -= fives
        return True
