class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        def dfs(person):
            searched.add(person)
            for richer in wealth_map[person]:
                if richer not in searched:
                    dfs(richer)
                if quiet[answer[richer]] < quiet[answer[person]]:
                    answer[person] = answer[richer]


        wealth_map = defaultdict(set)
        for a, b in richer:
            wealth_map[b].add(a)
        
        searched = set()
        answer = [i for i in range(len(quiet))]
        for person in range(len(quiet)):
            if person not in searched:
                dfs(person)
        return answer
