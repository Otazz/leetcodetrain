from typing import List
from math import floor, ceil


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
        
        idx = (i + j - 1) / 2
        return (nums3[floor(idx)] + nums3[ceil(idx)]) / 2

            
