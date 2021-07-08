class Solution:
    def trap(self, height: List[int]) -> int:
        idx_l, idx_r = 0, len(height) - 1
        h_l = h_r = 0
        total = 0
        
        while idx_l < idx_r:
            if height[idx_l] < height[idx_r]:
                if height[idx_l] < h_l:
                    total += h_l - height[idx_l]
                else:
                    h_l = height[idx_l]
                idx_l += 1
            else:
                if height[idx_r] < h_r:
                    total += h_r - height[idx_r]
                else:
                    h_r = height[idx_r]
                idx_r -= 1
        return total
        
        ## Solution 2: calculate water collected from both left and right side, 
        ## then choose the min one as final answer to current position
        # if height:
        #     h_left, h_right = height[0], height[-1]
        #     dp_l, dp_r = [0] * len(height), [0] * len(height)
        #     for i, h in enumerate(height):
        #         if h < h_left:
        #             dp_l[i] = h_left - h
        #         else:
        #             h_left = h
        #     for i in range(len(height)-1, -1, -1):
        #         if height[i] < h_right:
        #             dp_r[i] = h_right - height[i]
        #         else:
        #             h_right = height[i]
        #     for i, l, r in zip(range(len(height)), dp_l, dp_r):
        #         dp_l[i] = min(l, r) + dp_l[i-1] if i > 0 else min(l, r)
        #     return dp_l[-1]
        # return 0
