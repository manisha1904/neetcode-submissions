class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result :List[List[int]] = []
        nums_sorted = sorted(nums)
        for i, num in enumerate(nums_sorted):
            if num > 0:
                break
            if i > 0 and num == nums_sorted[i-1]:
                continue

            l, r = i+1, len(nums_sorted)-1
            while l < r:
                curr_sum = num + nums_sorted[l] + nums_sorted[r]
                if curr_sum == 0:
                    result.append([num, nums_sorted[l], nums_sorted[r]])
                    l += 1
                    r -= 1
                    while l < r and nums_sorted[l] == nums_sorted[l-1]:
                        l += 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    l += 1
        return result