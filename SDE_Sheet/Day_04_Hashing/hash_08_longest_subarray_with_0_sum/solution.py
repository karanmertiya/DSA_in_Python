# Time Complexity: O(N) (Constraint)
# Space Complexity: O(N) (Trade-off)
# Explanation: Store `prefix_sum` -> `index` in Hash Map. If sum repeats, calculate distance `i - hash[sum]`.

def max_len(arr: list[int]) -> int:
    prefix_index = {}
    max_len = sum = 0
    for i, num in enumerate(arr):
        sum += num
        if sum == 0:
            max_len = i + 1
        elif sum in prefix_index:
            max_len = max(max_len, i - prefix_index[sum])
        else:
            prefix_index[sum] = i
    return max_len

