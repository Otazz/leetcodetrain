from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0

        n1 = len(nums1)
        n2 = len(nums2)
        if n1 == 0:
            if (n2 - 1) % 2 == 0:
                return nums2[(n2 - 1) // 2]
        
            else:
                idx = (n2 - 1) // 2
                return (nums2[idx] + nums2[idx + 1]) / 2
        
        elif n2 == 0:
            if (n1 - 1) % 2 == 0:
                return nums1[(n1 - 1) // 2]
        
            else:
                idx = (n1 - 1) // 2
                return (nums1[idx] + nums1[idx + 1]) / 2

        while i < len(nums1):
            if nums1[i] > nums2[0]:
                nums1[i], nums2[0] = nums2[0], nums1[i]

                for j in range(1, len(nums2)):
                    if nums2[j] < nums2[j - 1]:
                        nums2[j], nums2[j - 1] = nums2[j - 1], nums2[j]

            i += 1
        

        if (n1 + n2 - 1) % 2 == 0:
            if (n1 + n2 - 1) // 2 < n1:
                return nums1[(n1 + n2 - 1) // 2]
            else:
                return nums2[(n1 + n2 - 1) // 2 - n1]
        
        else:
            idx = (n1 + n2 - 1) // 2

            return ((nums1[idx] if idx < n1 else nums2[idx - n1]) +
                    (nums1[idx + 1] if idx + 1 < n1 else nums2[idx + 1 - n1])) / 2
