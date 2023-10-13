class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # equals to bed_extend = [0] + flowerbed + [0]
        bed_extend = [0]
        bed_extend.extend(flowerbed)
        bed_extend.append(0)

        for i in range(1, len(bed_extend)-1):
            if not (bed_extend[i-1] or bed_extend[i] or bed_extend[i+1]):
                bed_extend[i] = 1
                n -= 1
        return n <= 0
