# Time Complexity: O(log(M * N))
# Space Complexity: O(1)
# Explanation: Treat the 2D matrix as a 1D flattened array. The element at `index` is at `matrix[index / cols][index % cols]`. Perform standard binary search.

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]: return False
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    while left <= right:
        mid = left + (right - left) // 2
        val = matrix[mid // n][mid % n]
        if val == target: return True
        if val < target: left = mid + 1
        else: right = mid - 1
    return False

