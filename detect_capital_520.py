class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        lower_word = word.lower()
        if word == lower_word or word == lower_word.capitalize() or word == lower_word.upper():
            return True
        return False
