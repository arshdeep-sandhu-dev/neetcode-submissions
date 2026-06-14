class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0
        for price in prices[1:]:
            profit = max(price-lowest, profit)
            lowest = min(lowest,price)
        return profit