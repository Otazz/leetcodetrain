from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        min_avg = 0
        n = len(nums)
        for i in range(len(nums)):
            diff = abs((sum(nums[:i+1]) // (i + 1)) - (sum(nums[i+1:]) // max(n - (i + 1), 1)))
            if i == 0:
                min_avg = diff
                idx = 0
            if diff < min_avg:
                min_avg = diff
                idx = i
        
        return idx

print(Solution().minimumAverageDifference([2,5,3,9,5,3]))