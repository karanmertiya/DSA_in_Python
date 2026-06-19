# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Maintain `min_price` seen so far and calculate potential profit for each day: `prices[i] - min_price`. Update `max_profit` if this profit is greater.

def maxProfit(prices: List[int]) -> int:
    minPrice, maxProf = float('inf'), 0
    for p in prices:
        minPrice = min(minPrice, p)
        maxProf = max(maxProf, p - minPrice)
    return maxProf

