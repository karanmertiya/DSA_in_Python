# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Explanation: Optimal: Group trains by platform. For each platform, this reduces to the Activity Selection Problem. Sort the trains by departure time and greedily pick non-overlapping trains.

def maxStop(trains, n, m):
    platforms = [[] for _ in range(m + 1)]
    for arr, dep, plat in trains:
        platforms[plat].append((dep, arr))
    count = 0
    for i in range(1, m + 1):
        if not platforms[i]: continue
        platforms[i].sort()
        count += 1
        lastDep = platforms[i][0][0]
        for j in range(1, len(platforms[i])):
            if platforms[i][j][1] >= lastDep:
                count += 1
                lastDep = platforms[i][j][0]
    return count

