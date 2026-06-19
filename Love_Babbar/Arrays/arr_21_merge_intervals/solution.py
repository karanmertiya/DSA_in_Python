# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Explanation: Sort the intervals based on the starting times. Iterate through the intervals, if the current interval overlaps with the last merged interval, update the end time of the last merged interval.

def merge(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals: return []
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

