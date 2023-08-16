class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        table = {(True, True): 'FizzBuzz',
                 (True, False): 'Fizz',
                 (False, True): 'Buzz',
                 (False, False): 1
        }

        for i in range(1, n + 1):
            mod3, mod5 = not bool(i % 3), not bool(i % 5)
            ans.append(str(table[(mod3, mod5)]))
            table[(False, False)] += 1
        return ans
