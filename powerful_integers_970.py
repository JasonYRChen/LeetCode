class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound == 0:
            return []

        x_power = floor(log(bound, x)) if x > 1 else 1
        y_power = floor(log(bound, y)) if y > 1 else 1

        return [n for n in {x**i + y**j for i in range(x_power+1) for j in range(y_power+1)} if n <= bound]
