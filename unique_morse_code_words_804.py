class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_codes = set()
        for word in words:
            code = ''
            for c in word:
                code += morse[ord(c) - ord('a')]
            morse_codes.add(code)
        return len(morse_codes)
