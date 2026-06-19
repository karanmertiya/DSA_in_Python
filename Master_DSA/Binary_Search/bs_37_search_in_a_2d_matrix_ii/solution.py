# Time Complexity: O(N + M)
# Space Complexity: O(1)
# Explanation: Start from the top-right corner. If `target == current`, return true. If `target < current`, move left (`c--`). If `target > current`, move down (`r++`).

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    r, c = 0, len(matrix[0]) - 1
    while r < len(matrix) and c >= 0:
        if matrix[r][c] == target: return True
        elif matrix[r][c] > target: c -= 1
        else: r += 1
    return False

