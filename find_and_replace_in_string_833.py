class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        replace = defaultdict(dict)
        for i, source, target in zip(indices, sources, targets):
            replace[i].update({source: target})
        new_s = ''
        i, prev_i = 0, 0
        while i < len(s):
            if i in replace:
                for source, target in replace[i].items():
                    if s[i:i+len(source)] == source:
                        new_s += target
                        i += len(source)
                        break
                else:
                    new_s += s[i]
                    i += 1
            else:
                new_s += s[i]
                i += 1
        return new_s
