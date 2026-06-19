# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Explanation: Sort the intervals based on the starting time. Create a result list and add the first interval. For subsequent intervals, if the current interval's start time is <= the last merged interval's end time, update the end time of the last merged interval to `max(last.end, current.end)`. Else, add the current interval to the result list.

def merge(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals: return []
    intervals.sort(key=lambda x: x[0])
    res = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1], intervals[i][1])
        else:
            res.append(intervals[i])
    return res

