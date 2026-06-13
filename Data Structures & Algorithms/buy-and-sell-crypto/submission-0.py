class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowest = prices[0]
        maxProfit = 0
        for i in range(1,len(prices)):
            sell = prices[i]
            maxProfit = max(maxProfit,sell-lowest)
            lowest = min(lowest,sell)
        return maxProfit