class Solution:
    def decodeString(self, s: str) -> str:
        from string import ascii_lowercase as al
        al = al + '['
        numbers = set("0123456789")

        queue = []
        num = 0
        i = 0
        while i < len(s):
            while s[i] in numbers:
                num = num * 10 + int(s[i])
                i += 1
            if num:
                queue.append(num)
                num = 0
            if s[i] in al:
                queue.append(s[i])
                i += 1
            if i < len(s) and s[i] == ']':
                word = ''
                while (token := queue.pop()) != '[':
                    word = token + word
                queue.append(word * queue.pop())
                i += 1
        return ''.join(queue)
