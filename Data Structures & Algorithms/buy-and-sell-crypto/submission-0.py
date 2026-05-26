class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length, result = len(prices), 0
        mx_right = [0] * length
        mx_right[length - 1] = prices[length - 1]
        for i in range(length-2, -1, -1):
            mx_right[i] = max(mx_right[i+1], prices[i])

        for i in range(length - 1):
            result = max(result, mx_right[i+1] - prices[i])
        return result
        