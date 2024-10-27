class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        index_list = defaultdict(list)
        for i, n in enumerate(nums):
            index_list[n].append(i)

        max_width = 0
        max_index = 0
        for n in sorted(index_list.keys(), reverse=True):
            max_index = max(max_index, index_list[n][-1])
            max_width = max(max_width, max_index - index_list[n][0])

        return max_width
