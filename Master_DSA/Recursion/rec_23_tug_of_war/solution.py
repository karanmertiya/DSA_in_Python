# Time Complexity: O(2^N)
# Space Complexity: O(N)
# Explanation: Keep track of the number of elements included in subset 1 and their sum. Recurse by including the current element in subset 1 or subset 2. Base case: if we reach end, check if subset 1 has `n/2` elements. If so, compute difference and update global minimum.

def tugOfWar(arr: List[int]) -> int:
    n = len(arr)
    totalSum = sum(arr)
    minDiff = [float('inf')]
    def solve(ind, cnt, sum1):
        if ind == n:
            if cnt == n // 2:
                sum2 = totalSum - sum1
                minDiff[0] = min(minDiff[0], abs(sum1 - sum2))
            return
        if cnt < n // 2:
            solve(ind + 1, cnt + 1, sum1 + arr[ind])
        solve(ind + 1, cnt, sum1)
    solve(0, 0, 0)
    return minDiff[0]

