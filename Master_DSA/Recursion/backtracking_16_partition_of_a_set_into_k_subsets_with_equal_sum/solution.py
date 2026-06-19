# Time Complexity: O(K^N)
# Space Complexity: O(N)
# Explanation: If total sum is not divisible by K, return false. Create an array of K subset sums. Backtrack to assign each element to one of the K subsets, ensuring no subset sum exceeds total_sum / K. To optimize, sort array descending.

def solve(a, k, target, subsetSum, idx):
    if idx == len(a):
        for s in subsetSum:
            if s != target: return False
        return True
    for i in range(k):
        if subsetSum[i] + a[idx] <= target:
            subsetSum[i] += a[idx]
            if solve(a, k, target, subsetSum, idx + 1): return True
            subsetSum[i] -= a[idx]
        if subsetSum[i] == 0: break
    return False

def isKPartitionPossible(a, k):
    total = sum(a)
    if total % k != 0: return False
    a.sort(reverse=True)
    subsetSum = [0] * k
    return solve(a, k, total // k, subsetSum, 0)

