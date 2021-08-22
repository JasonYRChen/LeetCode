from collections import deque, defaultdict


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        """
        The goal is to find the shortest sequences, just like finding the shortest
        path from node 'beginWord' to node 'endWord', so the core of the algorithm
        is BFS. One of the key points in code realization is to implement a suitable
        method to show only one character difference from current word. Take 'hot'  
        as example, we can save every word in wordList starts with 'h' and ends with
        't' in a dictionary with a key 'h.t' to specify each of these words is only
        one charactor difference from 'hot', and the difference is at the second
        charactor.
        """
        word_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '.' + word[i+1:]
                word_dict[key].append(word)

        result = []
        endWord_found = False
        dq = deque([[beginWord]])
        used = set()
        while dq and not endWord_found:
            temp = set()
            for _ in range(len(dq)):
                array = dq.popleft()
                last_word = array[-1]
                for i in range(len(last_word)):
                    key = last_word[:i] + '.' + last_word[i+1:]
                    if key not in used and key in word_dict:
                        temp.add(key)
                        for word in word_dict[key]:
                            if word == endWord:
                                endWord_found = True
                                result.append(array+[word])
                            else:
                                dq.append(array+[word])
            used.update(temp)
        return result

#        wordList.append(beginWord)
#        len_list = len(wordList)
#        indices = {word: i for i, word in enumerate(wordList)}
#        if endWord not in indices:
#            return []
#
#        is_next_word = [[False] * len_list for _ in range(len_list)]
 #       for word1 in wordList:
 #           for word2 in wordList:
 #               if self.is_one_diff(word1, word2):
 #                   row, col = indices[word1], indices[word2]
 #                   is_next_word[row][col] = is_next_word[col][row] = True
 #       
 #       result = []
 #       not_found = True
 #       words_remain = set(wordList) - {beginWord}
 #       dq = deque([[beginWord]])
 #       while dq and not_found:
 #           to_be_excluded = set()
 #           for _ in range(len(dq)):
 #               array = dq.popleft()
 #               last_word = array[-1]
 #               for next_word in words_remain:
 #                   row, col = indices[last_word], indices[next_word]
 #                   if is_next_word[row][col]:
 #                       new_array = array.copy()
 #                       new_array.append(next_word)
 #                       if next_word == endWord:
 #                           not_found = False
 #                           result.append(new_array)
 #                       else:
 #                           to_be_excluded.add(next_word)
 #                           dq.append(new_array)
 #           words_remain -= to_be_excluded
 #       return result
#
#    def is_one_diff(self, word1, word2):
#        count = 0
#        for char1, char2 in zip(word1, word2):
#            if char1 != char2:
#                count += 1
#        return count == 1


if __name__ == '__main__':
    import sys

    start = 'hit'
    end = 'cog'
    array = ["hot","dot","dog","lot","log","cog"] 
    print(Solution().findLadders(start, end, array))

