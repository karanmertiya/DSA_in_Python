# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Maintain 3 states: `hold` (holding a stock), `sold` (just sold, entering cooldown next), `rest` (not holding, not in cooldown). Transitions: `hold = max(hold, rest - price)`, `sold = hold + price`, `rest = max(rest, sold_prev)`.

def maxProfit(prices: List[int]) -> int:
    hold, sold, rest = float('-inf'), 0, 0
    for price in prices:
        prev_sold = sold
        sold = hold + price
        hold = max(hold, rest - price)
        rest = max(rest, prev_sold)
    return max(rest, sold)

