# Time Complexity: O(N^2) or worse
# Space Complexity: O(N) or O(1)
# Explanation: Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)

# TODO: Implement Brute Force
def smallestSubWithSum(arr, n, x):
    curr_sum = 0
    min_len = n + 1
    start, end = 0, 0
    while end < n:
        while curr_sum <= x and end < n:
            curr_sum += arr[end]
            end += 1
        while curr_sum > x and start < n:
            min_len = min(min_len, end - start)
            curr_sum -= arr[start]
            start += 1
    return 0 if min_len == n + 1 else min_len

# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Optimal: Use a sliding window. Add elements to `curr_sum` and increment `end`. When `curr_sum > x`, update `min_len` and subtract `arr[start]`, increment `start`.

def smallestSubWithSum(arr, n, x):
    curr_sum = 0
    min_len = n + 1
    start, end = 0, 0
    while end < n:
        while curr_sum <= x and end < n:
            curr_sum += arr[end]
            end += 1
        while curr_sum > x and start < n:
            min_len = min(min_len, end - start)
            curr_sum -= arr[start]
            start += 1
    return 0 if min_len == n + 1 else min_len

