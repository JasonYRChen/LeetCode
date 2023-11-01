class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        steps = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
        output = []
        for r in range(len(img)):
            output.append([])
            for c in range(len(img[0])):
                total = 0
                count = 0
                for r_step, c_step in steps:
                    if (0 <= r+r_step < len(img)) and (0 <= c+c_step < len(img[0])):
                        total += img[r+r_step][c+c_step]
                        count += 1
                output[-1].append(total // count)
        return output
