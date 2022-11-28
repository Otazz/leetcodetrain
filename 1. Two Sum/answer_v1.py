from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, target):
            left = 0
            right = len(nums) - 1

            while left <= right:
                middle = ((right - left) // 2) + left

                if nums[middle] == target:
                    return middle

                elif target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1

            return None
        
        idxs = {}

        for i in range(len(nums)):
            if nums[i] not in idxs:
                idxs[nums[i]] = [i]
            else:
                idxs[nums[i]].append(i)

        nums = sorted(nums)
        
        for i in range(len(nums)):
            diff = target - nums[i]
            left_idx = binarySearch(nums[:i], diff)

            if left_idx is not None:
                return [idxs[nums[i]][0], idxs[nums[left_idx]][0]] if nums[i] != nums[left_idx] else [idxs[nums[i]][0], idxs[nums[i]][1]]
            
            right_idx = binarySearch(nums[i:], diff)

            if right_idx is not None:
                return [idxs[nums[i]][0], idxs[nums[right_idx + i]][0]] if nums[i] != nums[right_idx + i] else [idxs[nums[i]][0], idxs[nums[i]][1]]
        
        return []

print(Solution().twoSum([3,3], 6))