class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_num = []
        for i in range(len(nums)):
            temp_num.append((nums[i], i))

        temp_num.sort()

        for i in range(len(nums)):
            val = target - temp_num[i][0]
            left, right = i+1, len(nums)-1
            while left <= right:
                mid :int = int((left + right) / 2)
                if val == temp_num[mid][0]:
                    return sorted([temp_num[i][1], temp_num[mid][1]])
                elif val < temp_num[mid][0]:
                    right = mid - 1
                else:
                    left = mid + 1

        
        return list([-1, -1])
        