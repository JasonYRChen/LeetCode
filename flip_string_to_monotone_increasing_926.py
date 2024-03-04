class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        counter = Counter(s)
        counter['1'] = 0
        min_flips = counter['0']
        for n in s:
            if n == '0':
                counter['0'] -= 1
            else:
                counter['1'] += 1
            min_flips = min(min_flips, counter['1'] + counter['0'])
        return min_flips
