class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        l, r = 0, m
        while l <= r:
            partA = (l + r) // 2
            partB = (m + n + 1) // 2 - partA

            leftA = nums1[partA - 1] if partA > 0 else float("-inf")
            rightA = nums1[partA] if partA < m else float("inf")
            leftB = nums2[partB - 1] if partB > 0 else float("-inf")
            rightB = nums2[partB] if partB < n else float("inf")

            if leftA <= rightB and leftB <= rightA:
                if (m + n) % 2 != 0:
                    return max(leftA, leftB)
                return (max(leftA, leftB) + min(rightA, rightB))/2
            elif leftA > rightB:
                r = partA - 1
            else:
                l = partA + 1