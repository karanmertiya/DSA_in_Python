# Time Complexity: O(N) (Constraint)
# Space Complexity: O(N) (Trade-off)
# Explanation: Optimal: Use a Prefix Sum and a Hash Set. If a prefix sum repeats, or equals 0, a 0-sum subarray exists between the identical prefix sums.

def has_zero_sum_subarray(arr: list[int]) -> bool:
    prefix_sums = set()
    curr_sum = 0
    for num in arr:
        curr_sum += num
        if curr_sum == 0 or curr_sum in prefix_sums:
            return True
        prefix_sums.add(curr_sum)
    return False

