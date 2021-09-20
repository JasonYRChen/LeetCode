class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s = {}
        mapping_t = {}
        for s_char, t_char in zip(s, t):
            if s_char not in mapping_s and t_char not in mapping_t:
                mapping_s[s_char], mapping_t[t_char] = t_char, s_char
            elif s_char not in mapping_s or mapping_s[s_char] != t_char:
                return False
        return True


if __name__ == '__main__':
    import sys

    print(Solution().isIsomorphic(sys.argv[1], sys.argv[2]))

