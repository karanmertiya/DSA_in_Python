# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1) (Constraint)
# Explanation: Fixed Sliding Window: Maintain a window of size K. Slide it by adding the next element and subtracting the first element of the previous window.

def maximum_sum_subarray(K: int, arr: list[int]) -> int:
    if len(arr) < K: return 0
    current_sum = sum(arr[:K])
    max_sum = current_sum
    for i in range(K, len(arr)):
        current_sum += arr[i] - arr[i-K]
        max_sum = max(max_sum, current_sum)
    return max_sum

