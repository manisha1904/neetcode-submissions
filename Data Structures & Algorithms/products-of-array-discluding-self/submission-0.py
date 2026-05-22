class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        complete_product = 1
        output_list = []
        zero_present = 0
        for num in nums:
            if num == 0:
                zero_present += 1
                continue
            complete_product *= num

        if zero_present > 1:
            return [0] * len(nums)

        for num in nums:
            if zero_present and num != 0:
                prod = 0
            elif num == 0:
                prod = complete_product
            else:
                prod = int(complete_product / num)
            output_list.append(prod)

        return output_list

        