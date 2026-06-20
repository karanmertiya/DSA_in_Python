# Time Complexity: O(N * M)
# Space Complexity: O(N * M) for output
# Explanation: Optimal: Maintain 4 pointers: top, bottom, left, right. Traverse Top row, Right col, Bottom row, Left col, shrinking boundaries inwards.

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    ans = []
    top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
    while top <= bottom and left <= right:
        for i in range(left, right+1): ans.append(matrix[top][i])
        top += 1
        for i in range(top, bottom+1): ans.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left-1, -1): ans.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top-1, -1): ans.append(matrix[i][left])
            left += 1
    return ans

