# Time Complexity: O(R * C)
# Space Complexity: O(C)
# Explanation: Treat each row as the base of a histogram. The height is the number of consecutive 1s going upwards. If a cell is 0, height is 0. For each row, after updating the heights, find the Largest Rectangle in Histogram (using a stack) and keep track of the maximum area overall.

def maximalRectangle(matrix):
    if not matrix: return 0
    r, c = len(matrix), len(matrix[0])
    heights = [0] * c
    max_area = 0
    def largestRectangleArea(h):
        st = []
        area = 0
        h.append(0)
        for i in range(len(h)):
            while st and h[st[-1]] >= h[i]:
                height = h[st.pop()]
                w = i if not st else i - st[-1] - 1
                area = max(area, height * w)
            st.append(i)
        h.pop()
        return area
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == '1': heights[j] += 1
            else: heights[j] = 0
        max_area = max(max_area, largestRectangleArea(heights))
    return max_area

