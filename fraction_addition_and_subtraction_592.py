class Solution:
    def fractionAddition(self, expression: str) -> str:
        left = 0
        signs = ['+']
        fractions = []
        # partition expression into fraction part and sign part
        for i in range(len(expression)):
            if (i + 1) == len(expression) or expression[i+1] == '+' or expression[i+1] == '-':
                fractions.append(expression[left:i+1])
                left = i + 2
                if (i + 1) != len(expression):
                    signs.append(expression[i+1])

        # fractions addition and subtraction
        numerator = 0
        denominator = 1
        for sign, fraction in zip(signs, fractions):
            n, d = fraction.split('/')
            n, d = int(n), int(d)
            n *= denominator
            denominator *= d
            numerator = numerator * d + n if sign == '+' else numerator * d - n

        gcd = math.gcd(numerator, denominator)
        return f'{numerator//gcd}/{denominator//gcd}'
