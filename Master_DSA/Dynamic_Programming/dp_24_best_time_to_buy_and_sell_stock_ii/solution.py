# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Add the profit whenever the price is higher than the previous day. This is equivalent to capturing every upward slope.

def maxProfit(prices: List[int]) -> int:
    return sum(max(prices[i] - prices[i-1], 0) for i in range(1, len(prices)))

