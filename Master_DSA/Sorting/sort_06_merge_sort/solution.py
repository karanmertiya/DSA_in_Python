# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Explanation: Divide and Conquer. Split array into halves until size 1. Merge sorted halves using a temporary array.

def mergeSort(arr: list[int]) -> list[int]:
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i]); i += 1
        else:
            res.append(right[j]); j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

