class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [n for n in nums if n != val]
        return len(nums)
        
        ## Another solution
        # k = 0
        # for num in nums:
        #     if num != val:
        #         nums[k] = num
        #         k += 1
        # return k
                
