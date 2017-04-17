class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        n = len(nums)
        if n < 4:
            return []
        nums.sort()
        i = 0
        while i < n:
            j = i + 1
            while j < n:
                l = j + 1
                r = n - 1
                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] < target:
                        l += 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                j += 1
                while j < n and nums[j - 1] == nums[j]:
                    j += 1
            i += 1
            while i < n and nums[i - 1] == nums[i]:
                i += 1
        return ans

s = Solution()
print(s.fourSum([1,0,-1,0,-2,2], 0))