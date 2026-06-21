# Time Complexity: O(N + M)
# Space Complexity: O(1)
# Explanation: Optimal: Use two pointers to traverse both sorted arrays simultaneously. Accumulate sums `sum1` and `sum2`. When elements match (intersection), add `max(sum1, sum2) + element` to the total answer and reset `sum1` and `sum2`. After the loop, add the remaining max sum.

def maxPathSum(arr1: List[int], arr2: List[int]) -> int:
    sum1 = sum2 = ans = 0
    i = j = 0
    n, m = len(arr1), len(arr2)
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            sum1 += arr1[i]
            i += 1
        elif arr1[i] > arr2[j]:
            sum2 += arr2[j]
            j += 1
        else:
            ans += max(sum1, sum2) + arr1[i]
            sum1, sum2 = 0, 0
            i += 1; j += 1
    while i < n:
        sum1 += arr1[i]
        i += 1
    while j < m:
        sum2 += arr2[j]
        j += 1
    ans += max(sum1, sum2)
    return ans

