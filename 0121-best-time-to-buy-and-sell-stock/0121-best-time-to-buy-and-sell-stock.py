class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n =len(prices)
        profit = 0
        min = float('inf')
        for i in prices:
            if i< min:
                min = i
            elif i-min > profit:
                profit= i-min
        return profit
        