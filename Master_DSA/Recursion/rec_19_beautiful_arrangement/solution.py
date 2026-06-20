# Time Complexity: O(K) where K is number of valid permutations
# Space Complexity: O(N)
# Explanation: Use an array to track visited numbers. Iterate from index 1 to n. For the current index, try placing an unvisited number. Check if the condition `(num % idx == 0 || idx % num == 0)` is met. If so, mark as visited, recurse to `idx + 1`, then backtrack.

def countArrangement(n: int) -> int:
    count = 0
    visited = [0] * (n + 1)
    def solve(idx):
        nonlocal count
        if idx > n:
            count += 1
            return
        for i in range(1, n + 1):
            if not visited[i] and (i % idx == 0 or idx % i == 0):
                visited[i] = 1
                solve(idx + 1)
                visited[i] = 0
    solve(1)
    return count

