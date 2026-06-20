# Time Complexity: O(N<sup>2</sup>) (Constraint)
# Space Complexity: O(1)
# Explanation: Takes an element and places it in its correct position within the previously sorted part of the array.

def insertion_sort(arr: list[int]) -> None:
    n = len(arr)
    for i in range(n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

