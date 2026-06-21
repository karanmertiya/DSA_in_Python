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

