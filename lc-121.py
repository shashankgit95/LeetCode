from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_purchase = prices[0]
        max_profit = 0

        for price in prices:
            best_purchase = min(price, best_purchase)
            max_profit = max(max_profit, price - best_purchase)
        
        return max_profit
        