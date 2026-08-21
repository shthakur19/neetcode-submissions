class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        profit = 0
        while r < len(prices):
            buy = prices[l]
            sell = max(prices[r:])
            profit = max(profit,sell - buy)
            l += 1
            r = l+1
        return profit


        

        