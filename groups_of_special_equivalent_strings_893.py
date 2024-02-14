class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        groups = set()
        for word in words:
            odd = sorted(word[::2])
            even = sorted(word[1::2])
            groups.add(''.join(odd) + ''.join(even))
        return len(groups)

        # solution 2
#        groups = []
#        for word in words:
#            odd_counter = Counter(word[::2])
#            even_counter = Counter(word[1::2])
#            for odd, even in groups:
#                if odd_counter == odd and even_counter == even:
#                    break
#            else:
#                groups.append((odd_counter, even_counter))
#        return len(groups)
