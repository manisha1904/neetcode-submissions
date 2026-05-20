class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_diff = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev_diff:
                return [prev_diff[diff], i]
            prev_diff[num] = i
        
        return []
        