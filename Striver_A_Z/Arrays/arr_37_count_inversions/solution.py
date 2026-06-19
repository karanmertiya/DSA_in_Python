# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Explanation: Use Merge Sort. During the merge step, if `arr[i] > arr[j]`, then there are `(mid - i + 1)` inversions because the left array is sorted, so all elements after `i` in the left array will also be greater than `arr[j]`.

def merge(arr, temp, left, mid, right):
    i, j, k = left, mid, left
    inv_count = 0
    while i <= mid - 1 and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            inv_count += (mid - i)
            j += 1
        k += 1
    while i <= mid - 1:
        temp[k] = arr[i]
        i += 1; k += 1
    while j <= right:
        temp[k] = arr[j]
        j += 1; k += 1
    for i in range(left, right + 1):
        arr[i] = temp[i]
    return inv_count

def mergeSort(arr, temp, left, right):
    inv_count = 0
    if right > left:
        mid = (right + left) // 2
        inv_count += mergeSort(arr, temp, left, mid)
        inv_count += mergeSort(arr, temp, mid + 1, right)
        inv_count += merge(arr, temp, left, mid + 1, right)
    return inv_count

def inversionCount(arr, n):
    temp = [0] * n
    return mergeSort(arr, temp, 0, n - 1)

