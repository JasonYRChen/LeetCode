class Solution:
    def evalRPN(self, tokens) -> int:
        operators = {'+': lambda x, y: x + y, 
                     '-': lambda x, y: x - y, 
                     '*': lambda x, y: x * y, 
                     '/': lambda x, y: x / y}
        stack = []
        for token in tokens:
            if token in operators:
                num_on_right = stack.pop()
                num_on_left = stack.pop()
                token = operators[token](num_on_left, num_on_right)
            stack.append(int(token))
        return stack[-1]


if __name__ == '__main__':
    t = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(Solution().evalRPN(t))
      
