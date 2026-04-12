class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = prices[0]
        for p in prices:
            if p > buy_price:
                diff = p - buy_price
                profit = max(profit, diff)
            else:
                buy_price = p
        if profit <=0:
            return 0
        else:
            return profit