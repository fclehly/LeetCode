class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans = ''
        i, j, c = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0:
            s = c
            if i >= 0:
                s += int(a[i])
            if j >= 0:
                s += int(b[j])
            ans = str(s % 2) + ans
            c = s // 2
            i -= 1
            j -= 1
        if c > 0:
            ans = '1' + ans
        return ans

s = Solution()
print(s.addBinary('11', '1'))
        
        


