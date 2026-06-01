class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        result = 0
        for i in range(length):
            height = heights[i]
            l = i - 1 if i >= 1 else i
            r = i + 1 if i < length - 1 else i
            # left 
            while l >= 0 and heights[l] >= height:
                l -= 1
            
            #right
            while r < length and heights[r] >= height:
                r += 1

            result = max(result, height * (r - l - 1))
        return result