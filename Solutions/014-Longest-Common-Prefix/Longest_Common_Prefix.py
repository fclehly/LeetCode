class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        for i in range(0, len(strs[0])):
            for s in strs:
                if i >= len(s) or strs[0][i] != s[i]:
                    return s[:i]
        return strs[0]

s = Solution()
print(s.longestCommonPrefix(["abab","aba",""]))