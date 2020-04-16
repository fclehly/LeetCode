from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        has_one = False
        for i in range(size):
            if nums[i] == 1:
                has_one = True
            elif nums[i] <= 0:
                nums[i] = 1
        if not has_one:
            return 1
        print(nums)
        for i in range(size):
            if abs(nums[i]) <= size:
                pos = abs(nums[i]) - 1
                nums[pos] = -abs(nums[pos])
        print(nums)
        for i in range(0, size):
            if nums[i] > 0:
                break
        return size + 1 if i + 1  == size and nums[size - 1] < 0 else i + 1

s = Solution()
print(s.firstMissingPositive([0,1, 3, 4]))