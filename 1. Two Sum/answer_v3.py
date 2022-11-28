from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxs = {}

        for i in range(len(nums)):
            if nums[i] not in idxs:
                idxs[nums[i]] = i
            elif not isinstance(idxs[nums[i]], list):
                idxs[nums[i]] = [idxs[nums[i]], i]
            else:
                idxs[nums[i]].append(i)

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in idxs:
                if diff != nums[i]:
                    return [i, idxs[diff]]
                if diff == nums[i] and isinstance(idxs[diff], list):
                    return [i, idxs[diff][-1]]

        return []

print(Solution().twoSum([3,3], 6))