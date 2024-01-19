class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        start = -1
        max_dis, temp_dis = 0, 0
        for i in range(len(seats)):
            if seats[i]:
                max_dis = max(max_dis, (i - start) // 2, temp_dis if start == -1 else 0)
                start = i
                temp_dis = 0
            else:
                temp_dis += 1
        return max(max_dis, temp_dis)
