def isValid(piles: List[int], h : int, mid: int) -> bool:
    for i in range(len(piles)):
        h -= ((piles[i] + mid - 1) // mid)
    return h >= 0 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            mid = (l + r) // 2
            if isValid(piles, h, mid):
                r = mid
            else:
                l = mid + 1

        return l
