class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        save = defaultdict(list)
        for s in strs:
            save[''.join(sorted(s))].append(s)
        return list(save.values())
