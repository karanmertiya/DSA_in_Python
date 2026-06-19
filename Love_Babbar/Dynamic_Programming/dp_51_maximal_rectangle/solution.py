# Time Complexity: O(R * C)
# Space Complexity: O(C)
# Explanation: Treat each row as the base of a histogram. Calculate heights for each row (`heights[j]++` if `matrix[i][j]=='1'`, else `0`). Then compute Largest Rectangle in Histogram for each row and take the maximum.

def maximalRectangle(matrix: List[List[str]]) -> int:
    if not matrix: return 0
    r, c = len(matrix), len(matrix[0])
    heights = [0] * c
    maxArea = 0
    for i in range(r):
        for j in range(c):
            heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
        st = []
        for j in range(c + 1):
            h = 0 if j == c else heights[j]
            while st and h < heights[st[-1]]:
                height = heights[st.pop()]
                width = j if not st else j - st[-1] - 1
                maxArea = max(maxArea, height * width)
            st.append(j)
    return maxArea

