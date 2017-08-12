class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        ans = 0
        maxLeft, maxRight = 0, 0
        while l <= r:
            if height[l] <= height[r]:
                if height[l] > maxLeft:
                    maxLeft = height[l]
                else:
                    ans += (maxLeft - height[l])
                l += 1
            else:
                if height[r] > maxRight:
                    maxRight = height[r]
                else:
                    ans += (maxRight - height[r])
                r -= 1
        return ans

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))