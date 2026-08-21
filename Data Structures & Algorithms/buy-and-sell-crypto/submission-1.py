class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        for i,n in enumerate(prices):
            buy = n
            while i < len(prices)-1:
                i = i+1
                profit = prices[i] - buy
                maxProfit = max(maxProfit, profit)
        return maxProfit
                

        