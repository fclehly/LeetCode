class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < 1 and n < k:
            return []
        ans = []
        temp = []
        def dfs(start, deep, max):
            # temp.append(start)
            if deep > 0:
                for i in range(start, max - deep + 2):
                    temp.append(i)
                    dfs(i + 1, deep - 1, max)
                    temp.pop()
            else:
                # print("d: " + str(temp))
                ans.append(temp[:])
        dfs(1, k, n)
        return ans
        
s = Solution()
print(s.combine(4, 3))