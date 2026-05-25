class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                curr_store = 0
                min_height = min(heights[i], heights[j])
                curr_store += (j - i) * min_height
                # for k in range(i, j):
                #     curr_store -= heights[k]
                result = max(result, curr_store)
        return result
