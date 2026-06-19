# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Use two pointers, left and right. Maintain left_max and right_max. If `arr[left] <= arr[right]`, the water trapped depends on left_max. If `arr[left] > left_max`, update left_max, else add `left_max - arr[left]` to answer and increment left. Repeat for right.

def trappingWater(arr, n):
    left, right = 0, n - 1
    left_max, right_max = 0, 0
    res = 0
    while left <= right:
        if arr[left] <= arr[right]:
            if arr[left] >= left_max: left_max = arr[left]
            else: res += left_max - arr[left]
            left += 1
        else:
            if arr[right] >= right_max: right_max = arr[right]
            else: res += right_max - arr[right]
            right -= 1
    return res

