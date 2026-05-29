class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        result = []
        for i in range(length-k+1):
            mx_value = float("-inf")
            for j in range(i, i+k):
                mx_value = max(mx_value, nums[j])
            result.append(mx_value)
        return result