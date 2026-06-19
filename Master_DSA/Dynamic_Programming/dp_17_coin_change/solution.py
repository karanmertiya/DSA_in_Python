# Time Complexity: O(N * Amount)
# Space Complexity: O(Amount)
# Explanation: Unbounded Knapsack variant. State `dp[amount]` stores min coins. Iterate through coins, and for each amount from `coin` to `target`, `dp[amt] = min(dp[amt], 1 + dp[amt - coin])`.

def coinChange(coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for amt in range(coin, amount + 1):
            dp[amt] = min(dp[amt], 1 + dp[amt - coin])
    return dp[amount] if dp[amount] != float('inf') else -1

