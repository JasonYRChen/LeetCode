class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for path in paths:
            files = path.split()
            for f in files[1:]:
                detail = f.split('(')
                mapping[detail[1][:-1]].append(f'{files[0]}/{detail[0]}')
        return [r for r in mapping.values() if len(r) > 1]
