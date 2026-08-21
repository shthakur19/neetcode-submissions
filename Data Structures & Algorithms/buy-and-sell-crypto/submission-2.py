class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l,r = 0,1
        while r < len(prices):
            buy = prices[l]
            sell = max(prices[r:])
            profit = sell - buy
            maxProfit = max(maxProfit, profit)
            l += 1
            r = l+1
        return maxProfit
                

        