# Time Complexity: O(N * 101)
# Space Complexity: O(N * 101)
# Explanation: Use a DP table `dp[i][mod]` to store the operator used to reach remainder `mod` at index `i`. Iterate through the array, for each reachable mod from previous step, try `(mod + arr[i]) % 101`, `(mod - arr[i]) % 101`, `(mod * arr[i]) % 101`. Then backtrack from `dp[N-1][0]` to find the operators.

def arithmeticExpressions(arr: List[int]) -> str:
    n = len(arr)
    dp = [[None] * 101 for _ in range(n)]
    dp[0][arr[0] % 101] = ('', 0)
    for i in range(1, n):
        for j in range(101):
            if dp[i-1][j] is not None:
                dp[i][(j + arr[i]) % 101] = ('+', j)
                dp[i][(j - arr[i] % 101 + 101) % 101] = ('-', j)
                dp[i][(j * arr[i]) % 101] = ('*', j)
    res = []
    curr = 0
    for i in range(n - 1, 0, -1):
        op, prev_mod = dp[i][curr]
        res.append(str(arr[i]))
        res.append(op)
        curr = prev_mod
    res.append(str(arr[0]))
    return "".join(reversed(res))

