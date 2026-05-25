class Solution:
    def trap(self, heights: List[int]) -> int:
        result = 0
        l, r = 0, len(heights)-1
        left_max, right_max = heights[0], heights[r]
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, heights[l])
                result += (left_max - heights[l])
            else:
                r -= 1
                right_max = max(right_max, heights[r])
                result += (right_max - heights[r])
        return result