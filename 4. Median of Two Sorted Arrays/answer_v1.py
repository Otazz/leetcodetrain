from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0

        nums3 = []

        while i < len(nums1) or j < len(nums2):
            if i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    nums3.append(nums1[i])
                    i += 1
                else:
                    nums3.append(nums2[j])
                    j += 1

            elif i < len(nums1):
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        
        if (i + j - 1) % 2 == 0:
            return nums3[(i + j - 1) // 2]
        
        else:
            idx = (i + j - 1) // 2
            return (nums3[idx] + nums3[idx + 1]) / 2
