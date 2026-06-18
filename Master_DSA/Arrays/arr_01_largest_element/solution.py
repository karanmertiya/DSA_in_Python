# Time Complexity: O(N log N) (Trade-off)
# Space Complexity: O(1)
# Explanation: Sort the array and return the last element.

def largest_element_brute(arr: list[int]) -> int:
    arr.sort()
    return arr[-1]

# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1)
# Explanation: Maintain a max variable and linearly scan the array updating it.

def largest_element_optimal(arr: list[int]) -> int:
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val

