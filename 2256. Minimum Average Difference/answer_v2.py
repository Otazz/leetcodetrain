from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        min_avg = 0
        n = len(nums)
        prefix = []
        suffix = []
        idx = 0
        sum_array = 0
        for i in range(len(nums)):
            sum_array += nums[i]
            prefix.append(sum_array)

        sum_array = 0
        for i in reversed(range(len(nums))):
            sum_array += nums[i]
            suffix.append(sum_array)

        for i in range(len(nums)):
            diff = abs(prefix[i] // (i + 1) - suffix[n - i - 2] // max(n - (i + 1), 1))
            if i == 0:
                min_avg = diff
                idx = 0
            if diff < min_avg:
                min_avg = diff
                idx = i

        if prefix[-1] // n < min_avg:
            return n - 1
        
        return idx

print(Solution().minimumAverageDifference([4,2,0]))