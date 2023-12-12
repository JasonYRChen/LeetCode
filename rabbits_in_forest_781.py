class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        total = 0
        for num, counts in counter.items():
            groups, residue = divmod(counts, num + 1)
            groups += 1 if residue else 0
            total += (num + 1) * groups
        return total
