# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Explanation: Use Merge Sort. While merging two sorted halves, if `left[i] > right[j]`, then all elements from `left[i]` to `left[mid]` will form inversions with `right[j]`.

def inversionCount(arr, n):
    temp = [0]*n
    def merge(left, mid, right):
        i, j, k, inv_count = left, mid, left, 0
        while i <= mid - 1 and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]; i += 1
            else:
                temp[k] = arr[j]; j += 1
                inv_count += (mid - i)
            k += 1
        while i <= mid - 1:
            temp[k] = arr[i]; i += 1; k += 1
        while j <= right:
            temp[k] = arr[j]; j += 1; k += 1
        for i in range(left, right + 1):
            arr[i] = temp[i]
        return inv_count
    def mergeSort(left, right):
        inv_count = 0
        if right > left:
            mid = (right + left) // 2
            inv_count += mergeSort(left, mid)
            inv_count += mergeSort(mid + 1, right)
            inv_count += merge(left, mid + 1, right)
        return inv_count
    return mergeSort(0, n - 1)

