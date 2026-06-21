# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Explanation: Optimal: Store pairs of (price, day). Sort by price. Greedily buy as many stocks as possible on the day with the lowest price, bounded by the maximum allowed on that day (which is 'day') and the remaining money.

def buyMaximumProducts(n, k, price):
    v = [(price[i], i + 1) for i in range(n)]
    v.sort()
    ans = 0
    for p, d in v:
        amount = min(d, k // p)
        ans += amount
        k -= amount * p
    return ans

