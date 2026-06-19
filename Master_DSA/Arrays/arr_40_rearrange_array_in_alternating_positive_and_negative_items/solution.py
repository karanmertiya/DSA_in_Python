# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Collect all positive numbers in one array and all negative numbers in another. Overwrite the original array by picking elements alternatively from the two arrays.

def rearrange(arr, n):
    pos = [x for x in arr if x >= 0]
    neg = [x for x in arr if x < 0]
    i, j, k = 0, 0, 0
    while i < len(pos) and j < len(neg):
        arr[k] = pos[i]; k += 1; i += 1
        arr[k] = neg[j]; k += 1; j += 1
    while i < len(pos):
        arr[k] = pos[i]; k += 1; i += 1
    while j < len(neg):
        arr[k] = neg[j]; k += 1; j += 1

