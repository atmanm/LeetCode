#Say you have an array for which the ith element is the price of a given stock
#on day i.
#If you were only permitted to complete at most one transaction (ie, buy one and
#sell one share of the stock), design an algorithm to find the maximum
#profit.
#Example
#Input: [7, 1, 5, 3, 6, 4]
#Output: 5
#max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than
#buying price)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        maxProfit = 0
        buyIdx = 0
        sellIdx = 1

        for idx in range(1, len(prices)):
            profit = prices[idx] - prices[buyIdx]

            if profit > maxProfit:
                maxProfit = profit
                sellIdx = idx
            elif profit < 0:
                buyIdx = idx

        return maxProfit

if __name__ == "__main__":
    try:
        prices = [int(x) for x in input().strip().split(',')]
    except ValueError:
        prices = []

    print(Solution().maxProfit(prices))
