class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        left, right = 0, len(people) - 1
        while left <= right:
            left += 1 if people[left] + people[right] <= limit else 0
            right -= 1
            boats += 1
        return boats
