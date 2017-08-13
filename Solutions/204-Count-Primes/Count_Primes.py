class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        res = 0
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, n // 2 + 1):
            if primes[i] == True:
                j = 2
                while i * j <= n:
                    primes[i * j] = False
                    j += 1
        for i in range(2, n):
            if primes[i] == True:
                res += 1
        return res

s = Solution()
# for i, flag in enumerate(s.countPrimes(2)):
#     print(i, flag)
print(s.countPrimes(5))