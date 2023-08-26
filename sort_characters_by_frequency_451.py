class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        array = [(v, k) for k, v in counter.items()]
        array.sort(reverse=True)
        return ''.join((v*k for v, k in array))
