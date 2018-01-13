#Say you have an array for which the ith element is the price of a given stock
#on day i.
#Design an algorithm to find the maximum profit. You may complete as many
#transactions as you like (ie, buy one and sell one share of the stock multiple
#times). However, you may not engage in multiple transactions at the same
#time (ie, you must sell the stock before you buy again).

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        maxProfit = 0
        buyIdx = 0
        sellIdx = 1
        curProfit = 0

        return sum(max(prices[i+1]-prices[i],0) for i in range(len(prices)-1))

if __name__ == "__main__":
    try:
        prices = [int(x) for x in input().strip().split(',')]
    except ValueError:
        prices = []

    print(Solution().maxProfit(prices))
