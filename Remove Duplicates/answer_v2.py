from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        while i <= len(nums) - 2:
            if nums[i] != nums[i+1]:
                nums[j] = nums[i+1]
                j += 1
            i += 1
        return j

print(Solution().removeDuplicates([1,1]))