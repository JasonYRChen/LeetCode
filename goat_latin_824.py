class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowel = {'a', 'e', 'i', 'o', 'u'}
        words = sentence.split()
        for i in range(len(words)):
            if words[i][0].lower() not in vowel:
                words[i] = words[i][1:] + words[i][0]
            words[i] += 'ma' + 'a' * (i + 1)
        return ' '.join(words)
