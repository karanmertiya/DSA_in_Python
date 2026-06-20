# Time Complexity: O(log(m * n))
# Space Complexity: O(1)
# Explanation: Optimal: Treat the 2D matrix as a 1D array and apply binary search. The element at `mid` can be accessed using `matrix[mid / cols][mid % cols]`.

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    if not matrix: return False
    m, n = len(matrix), len(matrix[0])
    low, high = 0, (m * n) - 1
    while low <= high:
        mid = (low + high) // 2
        if matrix[mid // n][mid % n] == target: return True
        if matrix[mid // n][mid % n] < target: low = mid + 1
        else: high = mid - 1
    return False

