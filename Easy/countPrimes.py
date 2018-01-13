#Count the number of prime numbers less than a non-negative number, n.

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        primes = [True] * n
        primes[0] = False
        primes[1] = False

        for i in range(2, int((n-1)**0.5)+1):
            primes[i*i:n:i] = [False] * len(primes[i*i:n:i])

        return sum(primes)

if __name__ == "__main__":
    n = int(input().strip())
    print(Solution().countPrimes(n))
