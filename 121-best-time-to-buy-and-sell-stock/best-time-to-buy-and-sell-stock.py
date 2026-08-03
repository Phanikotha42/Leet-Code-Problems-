class Solution(object):
    def maxProfit(self, prices):
        minPrice = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            else:
                profit1 = prices[i] - minPrice
                if profit1 > profit:
                    profit = profit1

        return profit

  


            

        