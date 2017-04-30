class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        i, j = 0, 0
        while i < len(nums) and j < len(nums):
            if nums[i] != nums[j]:
                nums[i] = nums[j]
            i += 1
            j += 1
            while j < len(nums) and nums[j] == nums[j - 1]:
                j += 1
                
        return i
        

s = Solution()
print(s.removeDuplicates([1, 1, 2, 3, 3]))