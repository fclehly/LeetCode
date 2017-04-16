class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ans = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[ans] = nums[i]
                ans += 1
        return ans
        

s = Solution()
print(s.removeElement([3, 1 ,2,2,3, 2], 3))