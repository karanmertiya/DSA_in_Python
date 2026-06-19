# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Explanation: Sort intervals based on start time. Push first interval to stack. For each subsequent interval, if it overlaps with the stack top, pop the stack top, merge the two, and push back. Else, push it to stack.

def merge(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals: return []
    intervals.sort(key=lambda x: x[0])
    st = [intervals[0]]
    for i in range(1, len(intervals)):
        if st[-1][1] >= intervals[i][0]:
            st[-1][1] = max(st[-1][1], intervals[i][1])
        else:
            st.append(intervals[i])
    return st

