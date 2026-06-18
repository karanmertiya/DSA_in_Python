# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1) (Constraint)
# Explanation: Maintain two variables, `largest` and `second_largest`. Update them simultaneously during a single pass.

def print2largest(arr: list[int]) -> int:
    largest = -1
    second_largest = -1
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest

