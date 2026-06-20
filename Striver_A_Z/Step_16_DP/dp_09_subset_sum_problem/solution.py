# Time Complexity: O(N * Sum)
# Space Complexity: O(Sum) space optimized
# Explanation: DP logic like 0/1 Knapsack. DP state is `dp[index][target]`. At each index, you can take or not take the element if `target >= arr[i]`.

def isSubsetSum(arr: List[int], sum: int) -> bool:
    n = len(arr)
    prev = [False] * (sum + 1)
    prev[0] = True
    if arr[0] <= sum: prev[arr[0]] = True
    for ind in range(1, n):
        cur = [False] * (sum + 1)
        cur[0] = True
        for target in range(1, sum + 1):
            notTaken = prev[target]
            taken = False
            if arr[ind] <= target: taken = prev[target - arr[ind]]
            cur[target] = notTaken or taken
        prev = cur
    return prev[sum]

