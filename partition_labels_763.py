class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ends = {c: i for i, c in enumerate(s)}
        partition = [-1]
        for i, c in enumerate(s):
            if i < partition[-1] and ends[c] > partition[-1]:
                partition[-1] = ends[c]
            elif i > partition[-1]:
                partition.append(ends[c])
        return [partition[i] - partition[i-1] for i in range(1, len(partition))]
