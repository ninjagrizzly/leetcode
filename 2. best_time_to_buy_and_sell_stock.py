# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

from typing import List

def maxProfit(prices: List[int]) -> int:
    if (len(prices) < 2):
        return 0

    min_price = prices[0]
    profit = 0

    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        else:
            profit = max(profit, prices[i] - min_price)
    
    return profit

print(maxProfit([7, 4, 5, 2, 1, 6, 10, 8, 12])) # 11