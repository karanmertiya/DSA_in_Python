# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Iterate through the array. If the value at `i` is equal to `i + 1`, append it to the result array.

def valueEqualToIndex(arr, n):
    ans = []
    for i in range(n):
        if arr[i] == i + 1:
            ans.append(arr[i])
    return ans

