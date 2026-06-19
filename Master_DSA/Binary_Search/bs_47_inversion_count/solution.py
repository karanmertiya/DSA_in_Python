# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Explanation: Modify Merge Sort. While merging two sorted halves, if `left[i] > right[j]`, then there are `mid - i + 1` inversions.

def inversionCount(arr: List[int], N: int) -> int:
    def mergeSort(arr, temp, left, right):
        inv_count = 0
        if right > left:
            mid = (left + right) // 2
            inv_count += mergeSort(arr, temp, left, mid)
            inv_count += mergeSort(arr, temp, mid + 1, right)
            inv_count += merge(arr, temp, left, mid + 1, right)
        return inv_count
    def merge(arr, temp, left, mid, right):
        inv_count = 0
        i, j, k = left, mid, left
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
    temp = [0] * N
    return mergeSort(arr, temp, 0, N - 1)

