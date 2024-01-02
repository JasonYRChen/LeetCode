class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        def word_count(tree, current_chars=0):
            if not tree:
                return 1, current_chars
            
            total_words = 0
            total_chars = 0
            for _, lower_level in tree.items():
                words, chars = word_count(lower_level, current_chars + 1)
                total_words += words
                total_chars += chars
            return total_words, total_chars


        tree = {}
        for word in words:
            node = tree
            for c in word[::-1]:
                if c not in node:
                    node[c] = {}
                node = node[c]
        total_words, total_chars = word_count(tree)
        return total_words + total_chars
