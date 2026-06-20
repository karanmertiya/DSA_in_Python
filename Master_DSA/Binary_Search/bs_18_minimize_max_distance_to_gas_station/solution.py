# Time Complexity: O(N^2) or worse
# Space Complexity: O(N) or O(1)
# Explanation: Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)

# TODO: Implement Brute Force
def findSmallestMaxDist(stations: List[int], k: int) -> float:
    def num_required(dist):
        cnt = 0
        for i in range(1, len(stations)):
            number_in_between = int((stations[i] - stations[i-1]) / dist)
            if (stations[i] - stations[i-1]) == (dist * number_in_between):
                number_in_between -= 1
            cnt += number_in_between
        return cnt
    low, high = 0, 0
    for i in range(len(stations) - 1):
        high = max(high, float(stations[i+1] - stations[i]))
    diff = 1e-6
    while high - low > diff:
        mid = low + (high - low) / 2.0
        if num_required(mid) > k: low = mid
        else: high = mid
    return high

# Time Complexity: O(N log(MaxDist / 1e-6))
# Space Complexity: O(1)
# Explanation: Optimal: Binary search on the real answer (distance) with a precision (e.g., 1e-6). For a given `mid` distance, count how many gas stations need to be inserted in each gap: `ceil((stations[i+1] - stations[i]) / mid) - 1`. If total needed > k, `low = mid`, else `high = mid`.

def findSmallestMaxDist(stations: List[int], k: int) -> float:
    def num_required(dist):
        cnt = 0
        for i in range(1, len(stations)):
            number_in_between = int((stations[i] - stations[i-1]) / dist)
            if (stations[i] - stations[i-1]) == (dist * number_in_between):
                number_in_between -= 1
            cnt += number_in_between
        return cnt
    low, high = 0, 0
    for i in range(len(stations) - 1):
        high = max(high, float(stations[i+1] - stations[i]))
    diff = 1e-6
    while high - low > diff:
        mid = low + (high - low) / 2.0
        if num_required(mid) > k: low = mid
        else: high = mid
    return high

