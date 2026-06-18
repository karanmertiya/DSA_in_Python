# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1)
# Explanation: Iterate while keeping track of the minimum price seen so far. Subtract this min from the current price to find potential profit.

def maxProfit(prices: list[int]) -> int:
    min_price = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        max_profit = max(max_profit, prices[i] - min_price)
        min_price = min(min_price, prices[i])
    return max_profit

