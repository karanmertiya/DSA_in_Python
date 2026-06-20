# Time Complexity: O(N^2) or worse
# Space Complexity: O(N) or O(1)
# Explanation: Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)

# TODO: Implement Brute Force
def findPair(arr, size, n):
    arr.sort()
    i, j = 0, 1
    while i < size and j < size:
        if i != j and arr[j] - arr[i] == n: return True
        elif arr[j] - arr[i] < n: j += 1
        else: i += 1
    return False

# Time Complexity: O(L log L)
# Space Complexity: O(1)
# Explanation: Optimal: Sort the array. Use two pointers `i = 0` and `j = 1`. If `arr[j] - arr[i] == N` and `i != j`, return true. If difference < N, `j++`. Else `i++`.

def findPair(arr, size, n):
    arr.sort()
    i, j = 0, 1
    while i < size and j < size:
        if i != j and arr[j] - arr[i] == n: return True
        elif arr[j] - arr[i] < n: j += 1
        else: i += 1
    return False

