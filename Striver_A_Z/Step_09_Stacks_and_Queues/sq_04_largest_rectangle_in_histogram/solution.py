# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Monotonic Stack. Find the next smaller element on the left and right for each bar. Area for bar `i` is `heights[i] * (right[i] - left[i] + 1)`. Alternatively, do it in a single pass stack loop.

def largestRectangleArea(heights: List[int]) -> int:
    n, maxArea = len(heights), 0
    st = []
    for i in range(n + 1):
        while st and (i == n or heights[st[-1]] >= heights[i]):
            height = heights[st.pop()]
            width = i if not st else i - st[-1] - 1
            maxArea = max(maxArea, width * height)
        st.append(i)
    return maxArea

