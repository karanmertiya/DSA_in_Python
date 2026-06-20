# Time Complexity: O(N * K)
# Space Complexity: O(N * K) or O(K)
# Explanation: If `k >= n/2`, it's equivalent to infinite transactions (Stock II). Else, use a DP array `dp[k][n]` where `dp[i][j]` is max profit using `i` transactions up to day `j`. Optimize inner loop by tracking `maxDiff = max(maxDiff, dp[i-1][j-1] - prices[j-1])`.

def maxProfit(k: int, prices: List[int]) -> int:
    n = len(prices)
    if n <= 1: return 0
    if k >= n // 2:
        return sum(max(prices[i] - prices[i-1], 0) for i in range(1, n))
    buy = [float('-inf')] * (k + 1)
    sell = [0] * (k + 1)
    for price in prices:
        for i in range(1, k + 1):
            buy[i] = max(buy[i], sell[i-1] - price)
            sell[i] = max(sell[i], buy[i] + price)
    return sell[k]

