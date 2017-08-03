# Python Solutin is out of time limit
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        if strs is None and len(strs) < 0:
            return []
        d = {}
        for s in strs:
            key = 1
            for c in s:
                key *= primes[ord(c) - ord('a')]
            if key in d.keys():
                d[key].append(s)
            else:
                d[key] = [s]
        return [value for value in d.values()]


s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


