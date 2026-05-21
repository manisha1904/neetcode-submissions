from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        result = []
        freq = [[] for i in range(len(nums) + 1)]

        for i in range(len(nums)):
            count[nums[i]] += 1

        for num, cnt in count.items():
            freq[cnt].append(num)

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
