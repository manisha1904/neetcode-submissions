class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        result = 0
        stack = []
        left_array, right_array = [-1] * length, [length] * length

        for i in range(length):
            height = heights[i]
            while stack and heights[stack[-1]] >= height:
                stack.pop()
            if stack:
                left_array[i] = stack[-1]
            stack.append(i) 

        stack = []
        for i in range(length - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right_array[i] = stack[-1]
            stack.append(i)
        
        for i in range(length):
            height = heights[i]
            result = max(result, height * (right_array[i] - left_array[i] - 1))
        return result