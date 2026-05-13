class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, best =  0, 1, 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            best = max(profit, best)
            
            if prices[r] < prices[l]:
                l = r
            r += 1

        return best





        