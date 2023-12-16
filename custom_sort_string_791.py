class Solution:
    def customSortString(self, order: str, s: str) -> str:
        result = ''
        counter = Counter(s)
        order_set = set(order)
        for c in chain(order, counter.keys()):
            result += c * counter[c]
            counter[c] = 0
        return result
