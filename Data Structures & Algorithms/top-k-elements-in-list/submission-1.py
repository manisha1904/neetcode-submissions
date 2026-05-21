from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        result = []
        heap = []
        for i in range(len(nums)):
            count[nums[i]] += 1

        for key, val in count.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)

        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result
