class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, len(prices)-1
        profit = 0
        while l < len(prices):
            buy = prices[l]
            while r > l:
                profit = max(profit, (prices[r]-buy))
                r -=1
            l += 1
            r = len(prices)-1

        return profit




        