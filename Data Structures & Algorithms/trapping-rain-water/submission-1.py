class Solution:
    def trap(self, heights: List[int]) -> int:
        result = 0
        ngl = [0] * len(heights)
        ngr = [0] * len(heights)
        ngl[0], ngr[len(heights)-1] = heights[0], heights[len(heights)-1]
        for i in range(1, len(heights)):
            ngl[i] = max(heights[i], ngl[i-1])
        for i in range(len(heights) - 2, -1, -1):
            ngr[i] = max(heights[i], ngr[i+1])

        for i in range(len(heights)):
            # if ngl[i] == -1 or ngr[i] == -1:
            #     continue
            result += min(ngl[i], ngr[i]) - heights[i]
        return result