class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        q_lcm = math.lcm(p, q)
        if not (q_lcm // q) % 2:
            return 2
        if not (q_lcm // p) % 2:
            return 0
        return 1
