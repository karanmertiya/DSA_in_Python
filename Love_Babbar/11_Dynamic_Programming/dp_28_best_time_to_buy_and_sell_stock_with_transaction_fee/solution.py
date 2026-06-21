# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Similar to Stock II, but subtract `fee` when selling. Maintain `cash` (max profit not holding stock) and `hold` (max profit holding stock). `cash = max(cash, hold + price - fee)`, `hold = max(hold, cash - price)`.

def maxProfit(prices: List[int], fee: int) -> int:
    cash, hold = 0, -prices[0]
    for i in range(1, len(prices)):
        cash = max(cash, hold + prices[i] - fee)
        hold = max(hold, cash - prices[i])
    return cash

