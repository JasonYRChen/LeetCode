class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Solution 1: do it backward
        for index in range(m + n):
            if m != 0 and (n == 0 or nums1[m-1] >= nums2[n-1]):
                nums1[-index-1] = nums1[m-1]
                m -= 1
            else:
                nums1[-index-1] = nums2[n-1]
                n -= 1
        
        # # Solution 2: do it forward
        # index1 = index2 = 0
        # if m > 0:
        #     nums1[-m:] = nums1[:m]
        # while (index := index1 + index2) < m + n:
        #     if index1 < m and (index2 == n or nums1[index1+n] <= nums2[index2]):
        #         nums1[index] = nums1[index1+n]
        #         index1 += 1
        #     else:
        #         nums1[index] = nums2[index2]
        #         index2 += 1

