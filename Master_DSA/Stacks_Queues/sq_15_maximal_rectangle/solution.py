# Time Complexity: O(rows * cols)
# Space Complexity: O(cols)
# Explanation: Treat each row as the base of a histogram. The height of each bar is the number of consecutive 1s above it. Apply the Largest Rectangle in Histogram algorithm for each row and maintain the maximum area.

def maximalRectangle(matrix):
    if not matrix: return 0
    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * cols
    maxArea = 0
    def largestRectangleArea(h):
        s, max_a = [], 0
        for i, val in enumerate(h + [0]):
            while s and h[s[-1]] >= val:
                height = h[s.pop()]
                width = i if not s else i - s[-1] - 1
                max_a = max(max_a, height * width)
            s.append(i)
        return max_a
    for row in matrix:
        for j in range(cols):
            heights[j] = heights[j] + 1 if row[j] == '1' else 0
        maxArea = max(maxArea, largestRectangleArea(heights))
    return maxArea

