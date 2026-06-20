# Time Complexity: O(N^2) or worse
# Space Complexity: O(N) or O(1)
# Explanation: Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)

# TODO: Implement Brute Force
def find_median(v):
    v.sort()
    n = len(v)
    if n % 2 != 0:
        return v[n // 2]
    else:
        return (v[n // 2 - 1] + v[n // 2]) // 2

# Time Complexity: O(N log N)
# Space Complexity: O(1)
# Explanation: Optimal: Sort the array. If the size is odd, the median is the middle element. If the size is even, the median is the average of the two middle elements.

def find_median(v):
    v.sort()
    n = len(v)
    if n % 2 != 0:
        return v[n // 2]
    else:
        return (v[n // 2 - 1] + v[n // 2]) // 2

