class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """ 
        ans = 0
        left = 0
        right = len(height) - 1
        while (left < right):
            area = min(height[left], height[right]) * (right - left)
            if ans < area:
                ans = area
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return ans

s = Solution()
print(s.maxArea([2, 2, 0, 1]))