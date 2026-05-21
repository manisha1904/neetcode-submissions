from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        nums_temp = []
        result = []
        for i in range(len(nums)):
            count[nums[i]] += 1

        for key, val in count.items():
            nums_temp.append((val, key))

        nums_temp.sort(reverse=True)

        for i in range(k):
            result.append(nums_temp[i][1])

        return result
