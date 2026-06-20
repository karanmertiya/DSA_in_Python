# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Two pointers `left` and `right`. Maintain `left_max` and `right_max`. Move the pointer pointing to the smaller max, adding trapped water.

def trap(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    res, maxLeft, maxRight = 0, 0, 0
    while left <= right:
        if height[left] <= height[right]:
            if height[left] >= maxLeft: maxLeft = height[left]
            else: res += maxLeft - height[left]
            left += 1
        else:
            if height[right] >= maxRight: maxRight = height[right]
            else: res += maxRight - height[right]
            right -= 1
    return res

