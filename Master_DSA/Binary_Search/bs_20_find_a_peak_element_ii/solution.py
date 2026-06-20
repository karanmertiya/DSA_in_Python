# Time Complexity: O(N^2) or worse
# Space Complexity: O(N) or O(1)
# Explanation: Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)

# TODO: Implement Brute Force
def findPeakGrid(mat: List[List[int]]) -> List[int]:
    n, m = len(mat), len(mat[0])
    low, high = 0, m - 1
    while low <= high:
        mid = (low + high) // 2
        max_row = 0
        for i in range(n):
            if mat[i][mid] > mat[max_row][mid]: max_row = i
        left = mat[max_row][mid-1] if mid - 1 >= 0 else -1
        right = mat[max_row][mid+1] if mid + 1 < m else -1
        if mat[max_row][mid] > left and mat[max_row][mid] > right:
            return [max_row, mid]
        elif mat[max_row][mid] < left:
            high = mid - 1
        else:
            low = mid + 1
    return [-1, -1]

# Time Complexity: O(N log M)
# Space Complexity: O(1)
# Explanation: Optimal: Binary search on columns. Find middle column, find max element in this column. Compare it with its left and right neighbors. If it's > both, it's a peak. If left is greater, peak exists in left half. Else, peak exists in right half.

def findPeakGrid(mat: List[List[int]]) -> List[int]:
    n, m = len(mat), len(mat[0])
    low, high = 0, m - 1
    while low <= high:
        mid = (low + high) // 2
        max_row = 0
        for i in range(n):
            if mat[i][mid] > mat[max_row][mid]: max_row = i
        left = mat[max_row][mid-1] if mid - 1 >= 0 else -1
        right = mat[max_row][mid+1] if mid + 1 < m else -1
        if mat[max_row][mid] > left and mat[max_row][mid] > right:
            return [max_row, mid]
        elif mat[max_row][mid] < left:
            high = mid - 1
        else:
            low = mid + 1
    return [-1, -1]

