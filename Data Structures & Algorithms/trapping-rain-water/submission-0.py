class Solution:
    def trap(self, heights: List[int]) -> int:
        result = 0
        for i in range(len(heights)):
            left_mx = max(heights[:i+1])
            right_mx = max(heights[i:])
            result += min(left_mx, right_mx) - heights[i]
        return result