class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict1 = {s: i for i, s in enumerate(list1)}
        dict2 = {s: i for i, s in enumerate(list2) if s in dict1}
        index_sum = defaultdict(list)
        for s in dict2.keys():
            index_sum[dict1[s] + dict2[s]].append(s)
        return index_sum[min(index_sum.keys())]
