class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dt = defaultdict(int)
        for num in nums:
            dt[num] += 1
            if dt[num] > 1:
                return num
        return -1