class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            temp = []
            while ans:
                array = ans.pop()
                new_array = array.copy()
                new_array.append(num)
                temp.append(array)
                temp.append(new_array)
            ans = temp
        return ans
