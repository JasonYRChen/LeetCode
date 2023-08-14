class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """ 
            Starts rearrangement from the highest, since the highest can not be affected by anyone in
            arrangement excecpt itselves. Then insert the rest of the heights in decreasing order into the
            queue by their k.
        """

        # solution 1
        people_dict = defaultdict(list)
        for h, k in people:
            people_dict[h].append(k)
        for array in people_dict.values():
            array.sort()
        sequence = sorted(people_dict.keys(), reverse=True)

        queue = []
        for h in sequence:
            for k in people_dict[h]:
                queue.insert(k, [h, k])
        return queue

        # solution2
        people.sort(key=lambda x: (-x[0], x[1]))

        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue
