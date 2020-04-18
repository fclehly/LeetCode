class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        if K % 2 == 0:
            last = self.kthGrammar(N - 1, K / 2)
            return 1 if last == 0 else 0
        else:
            last = self.kthGrammar(N - 1, (K + 1) / 2)
            return 1 if last == 1 else 0

s = Solution()
print(s.kthGrammar(4, 2))