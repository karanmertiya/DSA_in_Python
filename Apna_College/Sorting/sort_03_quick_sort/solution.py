# Time Complexity: O(N log N) Avg, O(N<sup>2</sup>) Worst
# Space Complexity: O(log N)
# Explanation: Divide and Conquer. Pick a pivot (e.g., first element), partition elements smaller to the left and larger to the right. Recurse.

def quickSort(arr: list[int], low: int, high: int):
    if low < high:
        pivot = arr[low]
        i, j = low, high
        while i < j:
            while arr[i] <= pivot and i <= high - 1: i += 1
            while arr[j] > pivot and j >= low + 1: j -= 1
            if i < j: arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        quickSort(arr, low, j - 1)
        quickSort(arr, j + 1, high)
    return arr

