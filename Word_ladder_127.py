from collections import deque, defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        # This is not the perfect version (see leetcode solution), but is still
        # good enough to compete 70% of other codes.
        word_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '.' + word[i+1:]
                word_dict[key].append(word)

        dq, used = deque([beginWord]), set()
        count = 1
        while dq:
            temp_used, temp_word = set(), set()
            temp_count = 0
            for _ in range(len(dq)):
                word = dq.popleft()
                for i in range(len(word)):
                    key = word[:i] + '.' + word[i+1:]
                    if key in word_dict and key not in used:
                        temp_used.add(key)
                        temp_count = 1
                        for next_word in word_dict[key]:
                            if next_word == endWord:
                                return count + 1
                            temp_word.add(next_word)
            if temp_count:
                count += 1
            else:
                return 0
            used.update(temp_used)
            dq.extend(temp_word)
        return count


if __name__ == '__main__':
    b = 'hit'
    e = 'cog'
    a = ["hot","dot","dog","lot","log","cog"]
    print(Solution().ladderLength(b, e, a))

