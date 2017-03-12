class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = '$#' + '#'.join(s) + "#_"
        p = [0] * 4096
        mx, id, mmax = 0, 0, 0
        for i in range(0, len(t) - 1):
            p[i] = min(p[2 * id - i], mx - i) if mx > i else 1
            while t[i + p[i]] == t[i - p[i]]:
                p[i] += 1
            if i + p[i] > mx:
                mx = i + p[i]
                id = i
            if p[mmax] < p[i]:
                mmax = i
        return s[(mmax - p[mmax]) // 2:(mmax + p[mmax] - 1) // 2]

s = Solution()
print("Testcase:")
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))
print(s.longestPalindrome('cccc'))
print(s.longestPalindrome('a'))