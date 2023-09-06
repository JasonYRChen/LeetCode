class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = defaultdict(lambda: -1)
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                mapping[stack.pop()] = num
            stack.append(num)
        return [mapping[n] for n in nums1]
