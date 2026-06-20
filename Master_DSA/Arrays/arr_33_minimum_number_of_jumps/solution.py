# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Optimal: Maintain `maxReach`, `steps`, and `jumps`. At each step `i`, `maxReach = max(maxReach, i + arr[i])`. Decrement `steps`. If `steps == 0`, `jumps++` and `steps = maxReach - i`. If `i >= maxReach`, return -1.

def minJumps(arr: List[int], n: int) -> int:
    if n <= 1: return 0
    if arr[0] == 0: return -1
    maxReach = steps = arr[0]
    jumps = 1
    for i in range(1, n):
        if i == n - 1: return jumps
        maxReach = max(maxReach, i + arr[i])
        steps -= 1
        if steps == 0:
            jumps += 1
            if i >= maxReach: return -1
            steps = maxReach - i
    return -1

