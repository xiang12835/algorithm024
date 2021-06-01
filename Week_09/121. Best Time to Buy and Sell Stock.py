class Solution:
    def maxProfit(self, prices):
        """
        T: O(n^2)
        S: O(1)
        """
        n = len(prices)
        max_profit = 0

        for i in range(n):
            for j in range(i+1, n):  # i+1 易错
                max_profit = max(max_profit, prices[j]-prices[i])

        return max_profit

class Solution:
    def maxProfit(self, prices):
        """
        min_price : 历史最低点
        max_profit : 最大利润

        T: O(n)
        S: O(1)
        """
        min_price = max(prices)
        max_profit = 0
        for p in prices:
            min_price = min(p, min_price)
            max_profit = max(p - min_price, max_profit)

        return max_profit
