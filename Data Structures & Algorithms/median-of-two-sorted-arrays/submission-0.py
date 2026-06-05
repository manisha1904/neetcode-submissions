class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        prev = curr = 0
        i = j = 0
        for _ in range((m + n) // 2 + 1):
            prev = curr

            if i < m and (j >= n or nums1[i] <= nums2[j]):
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1
        
        if (m + n) % 2 != 0:
            return curr
        return (prev + curr) / 2