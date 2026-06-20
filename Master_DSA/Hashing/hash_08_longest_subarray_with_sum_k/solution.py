# Time Complexity: O(N^2) or worse
# Space Complexity: O(N) or O(1)
# Explanation: Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)

# TODO: Implement Brute Force
def len_of_long_subarr(arr: list[int], k: int) -> int:
    prefix_index = {}
    max_len = sum = 0
    for i, num in enumerate(arr):
        sum += num
        if sum == k:
            max_len = i + 1
        needed = sum - k
        if needed in prefix_index:
            max_len = max(max_len, i - prefix_index[needed])
        if sum not in prefix_index:
            prefix_index[sum] = i
    return max_len

# Time Complexity: O(N) (Constraint)
# Space Complexity: O(N) (Trade-off)
# Explanation: Optimal: Prefix Sum Map storing indices. Check if `sum - K` exists in map and calculate index difference.

def len_of_long_subarr(arr: list[int], k: int) -> int:
    prefix_index = {}
    max_len = sum = 0
    for i, num in enumerate(arr):
        sum += num
        if sum == k:
            max_len = i + 1
        needed = sum - k
        if needed in prefix_index:
            max_len = max(max_len, i - prefix_index[needed])
        if sum not in prefix_index:
            prefix_index[sum] = i
    return max_len

