# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Use a stack to keep track of the indices of the bars in increasing order of height. If the current bar is shorter than the top of the stack, pop bars and calculate the area for each popped bar as the shortest bar. The width is `i - stack.top() - 1`. If stack is empty, width is `i`.

def largestRectangleArea(heights):
    s, maxArea = [], 0
    for i, h in enumerate(heights + [0]):
        while s and heights[s[-1]] >= h:
            height = heights[s.pop()]
            width = i if not s else i - s[-1] - 1
            maxArea = max(maxArea, height * width)
        s.append(i)
    return maxArea

