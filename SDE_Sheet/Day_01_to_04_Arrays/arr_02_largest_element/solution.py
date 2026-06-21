# Time Complexity: O(N log N)
# Space Complexity: O(1) or O(N) depending on sort
# Explanation: Brute Force: Sort the array and return the last element.

def largest(arr: list[int]) -> int:
    arr.sort()
    return arr[-1]

# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1) (Constraint)
# Explanation: Optimal: Iterate through the array maintaining a variable for the maximum element seen so far.

def largest(arr: list[int]) -> int:
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

