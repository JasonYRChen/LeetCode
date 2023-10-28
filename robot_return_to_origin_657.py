lass Solution:
    def judgeCircle(self, moves: str) -> bool:
        # version 2
        counter = defaultdict(int)
        for s in moves:
            counter[s] += 1
        return (counter['U'] == counter['D']) and (counter['L'] == counter['R'])

        # version 1
#        counter = {'UD': 0, 'LR': 0}
#        for s in moves:
#            if s in 'UD':
#                counter['UD'] += 1 if s == 'U' else -1
#            else:
#                counter['LR'] += 1 if s == 'L' else -1
#        return not (counter['UD'] or counter['LR'])
