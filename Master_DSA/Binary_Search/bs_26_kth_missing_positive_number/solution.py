# Time Complexity: O(log N)
# Space Complexity: O(1)
# Explanation: At any index `i`, the number of missing elements before `arr[i]` is `arr[i] - (i + 1)`. Use binary search to find the index where the number of missing elements becomes `>= k`. The answer will be `low + k`.

def findKthPositive(arr, k):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        missing = arr[mid] - (mid + 1)
        if missing < k: low = mid + 1
        else: high = mid - 1
    return low + k

