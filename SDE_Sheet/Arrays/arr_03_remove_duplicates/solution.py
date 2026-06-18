# Time Complexity: O(N log N) (Trade-off)
# Space Complexity: O(N) (Trade-off)
# Explanation: Use an auxiliary HashSet to store unique elements, then put them back.

def remove_duplicates_brute(arr: list[int]) -> int:
    unique_set = sorted(set(arr))
    for i in range(len(unique_set)):
        arr[i] = unique_set[i]
    return len(unique_set)

# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1) (Constraint)
# Explanation: Two-pointer approach: Place unique elements at the `i` pointer while `j` scans.

def remove_duplicates_optimal(arr: list[int]) -> int:
    if not arr: return 0
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i + 1

