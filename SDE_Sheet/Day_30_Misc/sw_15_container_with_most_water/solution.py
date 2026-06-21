# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Two Pointers from ends. Area is `min(h[left], h[right]) * width`. Move the pointer with the smaller height to seek a potentially taller line.

def maxArea(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

