class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result, length = 0, len(prices)
        buy_price = prices[0]
        for sell in prices:
            result = max(result, sell - buy_price)
            buy_price = min(buy_price, sell)
        return result
        