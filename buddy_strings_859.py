class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        same_char = defaultdict(int)
        different_char = defaultdict(int)
        different_count = 0
        for cs, cg in zip(s, goal):
            if cs == cg:
                same_char[cs] += 1
            else:
                different_char[cs] += 1
                different_char[cg] -= 1
                different_count += 1
                
        any_same_char = any(map(lambda x: same_char[x] > 1, same_char.keys()))
        no_difference = all(map(lambda x: not different_char[x], different_char.keys()))
        valid_difference = no_difference and different_count == 2
        valid_swap = any_same_char and not different_count
        if len(s) == len(goal) and (valid_difference or valid_swap):
            return True
        return False
