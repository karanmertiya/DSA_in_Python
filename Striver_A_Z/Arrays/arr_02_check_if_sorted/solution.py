# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1)
# Explanation: Linearly traverse and ensure `arr[i] <= arr[i+1]`.

def is_sorted(arr: list[int]) -> bool:
    if len(arr) <= 1: return True
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

