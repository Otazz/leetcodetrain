from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        total_duplicates = 0
        i = 0
        while i + total_duplicates < len(nums) - 1:
            duplicate = 0
            while (i+duplicate+1) < len(nums) - total_duplicates and nums[i+duplicate+1] == nums[i]:
                duplicate += 1
            for j in range(i + 1, len(nums) - duplicate):
                nums[j] = nums[j+duplicate]
            total_duplicates += duplicate
            i += 1
        return len(nums) - total_duplicates

print(Solution().removeDuplicates([1,1]))