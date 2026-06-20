# Time Complexity: O(N<sup>2</sup>) (Constraint)
# Space Complexity: O(1) (Constraint)
# Explanation: Find the minimum element in the unsorted array and swap it with the element at the beginning.

def selection_sort(arr: list[int]) -> None:
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

