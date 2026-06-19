# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Explanation: Sort the intervals based on the starting time. Then iterate and merge if the current interval's start is <= the last merged interval's end.

def merge(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals: return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for interval in intervals[1:]:
        if merged[-1][1] >= interval[0]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)
    return merged

