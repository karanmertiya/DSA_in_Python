# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Explanation: Sort the intervals by their start times. Iterate through them. If the result list is empty or the current interval's start is > the last interval's end, append it. Otherwise, update the last interval's end to the maximum of its end and current end.

def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

