from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxs = {}

        for i in range(len(nums)):
            if nums[i] not in idxs:
                idxs[nums[i]] = [i]
            else:
                idxs[nums[i]].append(i)

        for i in range(len(nums)):
            curr_number = nums[i]
            diff = target - curr_number

            if diff in idxs:
                if diff != curr_number or (diff == curr_number and len(idxs[curr_number]) > 1):
                    return [i, idxs[diff][-1]]

        return []

print(Solution().twoSum([3,2,4], 6))