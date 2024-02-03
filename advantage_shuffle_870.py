class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        candidates = deque(sorted(nums1))
        indices = defaultdict(list)
        for i, num in enumerate(nums2):
            indices[num].append(i)
        targets = sorted(indices.keys(), reverse=True)
        
        for target in targets:
            for index in indices[target]:
                nums2[index] = candidates.pop() if target < candidates[-1] else candidates.popleft()
        return nums2
