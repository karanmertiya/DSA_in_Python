# Time Complexity: O(N^2) or worse
# Space Complexity: O(N) or O(1)
# Explanation: Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)

# TODO: Implement Brute Force
def maxMeetings(N, S, F):
    m = [(S[i], F[i], i + 1) for i in range(N)]
    m.sort(key=lambda x: (x[1], x[2]))
    ans = [m[0][2]]
    last_e = m[0][1]
    for i in range(1, N):
        if m[i][0] > last_e:
            ans.append(m[i][2])
            last_e = m[i][1]
    ans.sort()
    return ans

# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Explanation: Optimal: Store `(start, end, index)`. Sort by end time. Pick the first meeting. For subsequent meetings, if `start > last_picked_end`, pick it and update `last_picked_end`. Return sorted indices.

def maxMeetings(N, S, F):
    m = [(S[i], F[i], i + 1) for i in range(N)]
    m.sort(key=lambda x: (x[1], x[2]))
    ans = [m[0][2]]
    last_e = m[0][1]
    for i in range(1, N):
        if m[i][0] > last_e:
            ans.append(m[i][2])
            last_e = m[i][1]
    ans.sort()
    return ans

