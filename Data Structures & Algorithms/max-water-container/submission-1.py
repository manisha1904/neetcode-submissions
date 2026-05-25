class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         curr_store = 0
        #         min_height = min(heights[i], heights[j])
        #         curr_store += (j - i) * min_height
        #         result = max(result, curr_store)
        l, r = 0, len(heights) - 1
        while l < r:
            curr_store = min(heights[l], heights[r]) * (r - l)
            result = max(result, curr_store)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return result
