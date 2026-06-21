# Time Complexity: O(N)
# Space Complexity: O(N) recursive stack
# Explanation: Swap `arr[l]` and `arr[r]` and then recursively call `reverse(arr, l+1, r-1)`.

def reverseArray(arr, l, r):
    if l >= r: return
    arr[l], arr[r] = arr[r], arr[l]
    reverseArray(arr, l + 1, r - 1)

