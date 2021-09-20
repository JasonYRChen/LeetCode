class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [0, 0] + [1] * (n - 2)
        for i in range(2, int(n**0.5)+1):
            if primes[i]:
                primes[i**2::i] = [0] * len(primes[i**2::i])
        return sum(primes)


if __name__ == '__main__':
    import sys

    print(Solution().countPrimes(int(sys.argv[1])))

