class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        for num in nums1:
            dict1[num] += 1
        for num in nums2:
            dict2[num] += 1
        commons = set(dict1.keys()) & set(dict2.keys())
        return [i for i in commons for _ in range(min(dict1[i], dict2[i]))]
