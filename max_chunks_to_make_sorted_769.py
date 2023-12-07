class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        target = arr[0]
        for i, num in enumerate(arr):
            if num > target:
                target = num
            elif target == i:
                chunks += 1
                target = arr[i+1] if i + 1 < len(arr) else target
        return chunks
