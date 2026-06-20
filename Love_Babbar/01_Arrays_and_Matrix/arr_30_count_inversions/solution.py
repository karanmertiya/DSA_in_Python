# Time Complexity: O(N log N)
# Space Complexity: O(N) auxiliary
# Explanation: Optimal: Merge Sort approach. While merging two sorted halves, if left[i] > right[j], it forms an inversion with all remaining elements in the left half (mid - i + 1).

def inversionCount(arr: List[int], n: int) -> int:
    def merge(low, mid, high):
        temp, left, right, cnt = [], low, mid + 1, 0
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left]); left += 1
            else:
                temp.append(arr[right]); cnt += (mid - left + 1); right += 1
        while left <= mid: temp.append(arr[left]); left += 1
        while right <= high: temp.append(arr[right]); right += 1
        for i in range(low, high + 1): arr[i] = temp[i - low]
        return cnt
    def mergeSort(low, high):
        cnt = 0
        if low >= high: return cnt
        mid = (low + high) // 2
        cnt += mergeSort(low, mid)
        cnt += mergeSort(mid + 1, high)
        cnt += merge(low, mid, high)
        return cnt
    return mergeSort(0, n - 1)

