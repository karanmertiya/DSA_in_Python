# Time Complexity: O(N * M)
# Space Complexity: O(M)
# Explanation: Maintain a histogram for each row. The height of the histogram is the consecutive 1s ending at that cell. For each row's histogram, use the 'Largest Rectangle in Histogram' stack algorithm.

def maximalRectangle(matrix: List[List[str]]) -> int:
    if not matrix: return 0
    def largestRectangleArea(heights):
        st = []
        maxA = 0
        heights.append(0)
        for i, h in enumerate(heights):
            while st and heights[st[-1]] >= h:
                height = heights[st.pop()]
                w = i if not st else i - st[-1] - 1
                maxA = max(maxA, height * w)
            st.append(i)
        return maxA
    
    maxArea = 0
    heights = [0] * len(matrix[0])
    for row in matrix:
        for j, val in enumerate(row):
            heights[j] = heights[j] + 1 if val == '1' else 0
        maxArea = max(maxArea, largestRectangleArea(heights))
    return maxArea

