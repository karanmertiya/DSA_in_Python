# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Use the array elements as indices. For each element `abs(Arr[i])`, negate the value at index `abs(Arr[i]) - 1`. If the value is already negative, it's the repeating element. After the loop, the index with a positive value corresponds to the missing element.

def findTwoElement(arr, n):
    ans = [0, 0]
    for i in range(n):
        val = abs(arr[i])
        if arr[val - 1] < 0: ans[0] = val
        else: arr[val - 1] = -arr[val - 1]
    for i in range(n):
        if arr[i] > 0:
            ans[1] = i + 1
            break
    return ans

