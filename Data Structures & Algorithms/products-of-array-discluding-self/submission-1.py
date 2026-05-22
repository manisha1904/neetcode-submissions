class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       output_list = [1] * len(nums)
       prefix, postfix = 1, 1
       for i in range(len(nums)):
            output_list[i] *= prefix
            prefix *= nums[i]

       for i in range(len(nums) - 1, -1, -1):
            output_list[i] *= postfix
            postfix *= nums[i]

       return output_list

        