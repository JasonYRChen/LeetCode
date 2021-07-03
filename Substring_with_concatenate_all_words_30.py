class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        len_w = len(words[0])
        words_dict = defaultdict(int)
        for word in words:
            words_dict[word] += 1
        
        indices = []
        for start in range(len_w):  # deal with word like 'aa' or 'abab' repeating substring inside itself
            idx = start
            while idx < (len(s) - len_w * len(words) + 1):
                temp_dict = defaultdict(int)
                j = 0
                while (word := s[idx+j*len_w: idx+(j+1)*len_w]) in words_dict:
                    if word in temp_dict and temp_dict[word] == words_dict[word]:
                        temp_dict[s[idx: idx+len_w]] -= 1
                        j -= 1
                        idx += len_w
                    else:
                        temp_dict[word] += 1
                        j += 1
                        if j == len(words):
                            indices.append(idx)
                idx += (j + 1) * len_w
        return indices

