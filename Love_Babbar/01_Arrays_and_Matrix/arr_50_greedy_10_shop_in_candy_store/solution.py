# Time Complexity: O(N log N)
# Space Complexity: O(1)
# Explanation: Optimal: Sort the candies by price. For minimum cost, buy the cheapest and take K most expensive for free. For maximum cost, buy the most expensive and take K cheapest for free.

def candyStore(candies, N, K):
    candies.sort()
    minCost, maxCost = 0, 0
    i, j = 0, N - 1
    while i <= j:
        minCost += candies[i]
        i += 1; j -= K
    i, j = N - 1, 0
    while j <= i:
        maxCost += candies[i]
        i -= 1; j += K
    return [minCost, maxCost]

