class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        counter = Counter(arr)
        candidates = sorted(counter.keys())
        total = 0
        for i in range(len(candidates)):
            for j in range(i, len(candidates)):
                third = target - candidates[i] - candidates[j]
                if third in counter and third >= candidates[j]:
                    temp = Counter([candidates[i], candidates[j], third])
                    number = 1
                    for k, v in temp.items():
                        if v > counter[k]:
                            break
                        number *= comb(counter[k], v)
                    else:
                        total += number
        return total % (10 ** 9 + 7)
