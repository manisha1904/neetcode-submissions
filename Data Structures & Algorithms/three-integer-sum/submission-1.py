class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result :List[List[int]] = []
        nums_sorted = sorted(nums)
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        for i in range(len(nums_sorted)):
            count[nums_sorted[i]] -= 1
            if i and nums_sorted[i] == nums_sorted[i-1]:
                continue

            for j in range(i+1, len(nums_sorted)):
                count[nums_sorted[j]] -= 1
                if j-1 > i and nums_sorted[j] == nums_sorted[j-1]:
                    continue
                target = -(nums_sorted[i] + nums_sorted[j])
                if count[target] > 0:
                    result.append([nums_sorted[i], nums_sorted[j], target])

            for j in range(i+1, len(nums_sorted)):
                count[nums_sorted[j]] += 1
        return result