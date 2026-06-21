# Time Complexity: O(N log(Max-Min))
# Space Complexity: O(1)
# Explanation: Binary search on the value range `[matrix[0][0], matrix[n-1][n-1]]`. Count elements less than or equal to `mid` using two pointers (start from bottom-left). If count >= k, search left half, else search right.

def kthSmallest(matrix: List[List[int]], k: int) -> int:
    n = len(matrix)
    def countLessOrEqual(mid):
        count, r, c = 0, n - 1, 0
        while r >= 0 and c < n:
            if matrix[r][c] <= mid:
                count += r + 1
                c += 1
            else:
                r -= 1
        return count
    low, high = matrix[0][0], matrix[-1][-1]
    while low <= high:
        mid = low + (high - low) // 2
        if countLessOrEqual(mid) >= k:
            high = mid - 1
        else:
            low = mid + 1
    return low

