from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = 0
        suffix = sum(nums)
        idx = 0

        for i in range(len(nums)):
            prefix += nums[i]
            suffix -= nums[i]
            diff = suffix // (n - (i + 1)) if n > (i + 1) else suffix
            diff = abs(prefix // (i + 1) - diff)
            if i == 0:
                min_avg = diff
                idx = 0
            if diff < min_avg:
                min_avg = diff
                idx = i
        
        return idx

print(Solution().minimumAverageDifference([4,2,0]))