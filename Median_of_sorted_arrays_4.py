class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Running time: O(n+m), space: O(1)
        current = prev = 0
        idx1 = idx2 = 0
        mid, is_odd = divmod((len(nums1) + len(nums2)), 2)
        while idx1 + idx2 <= mid:
            if idx2 == len(nums2) or (idx1 < len(nums1) and nums1[idx1] <= nums2[idx2]):
                current, prev = nums1[idx1], current
                idx1 += 1
            else:
                current, prev = nums2[idx2], current
                idx2 += 1
        if is_odd:
            return current
        return (current + prev) / 2
