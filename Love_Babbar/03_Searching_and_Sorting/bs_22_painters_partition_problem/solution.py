# Time Complexity: O(N log(Sum-Max))
# Space Complexity: O(1)
# Explanation: Optimal: Identical to Allocate Books and Split Array Largest Sum. Binary search `max(boards)` to `sum(boards)`.

def findLargestMinDistance(boards: List[int], k: int) -> int:
    def count_painters(time):
        painters, boards_painter = 1, 0
        for b in boards:
            if boards_painter + b <= time:
                boards_painter += b
            else:
                painters += 1
                boards_painter = b
        return painters
    low, high = max(boards), sum(boards)
    while low <= high:
        mid = low + (high - low) // 2
        if count_painters(mid) > k: low = mid + 1
        else: high = mid - 1
    return low

