class Solution:
    def countAndSay(self, n: int) -> str:
        a = [''] * n
        a[0] = '1'
        for i in range(1, n):
            s = a[i - 1]
            j = k = 0
            temp = []
            while k < len(s):
                count = 0
                while k < len(s) and s[k] == s[j]:
                    k += 1
                    count += 1
                temp.append(str(count))
                temp.append(s[j])
                j = k
            a[i] = ''.join(temp)
        print(a)
        return a[n - 1]
            
s = Solution()
print(s.countAndSay(10))