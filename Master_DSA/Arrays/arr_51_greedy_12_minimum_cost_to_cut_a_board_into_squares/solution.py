# Time Complexity: O(N^2) or worse
# Space Complexity: O(N) or O(1)
# Explanation: Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)

# TODO: Implement Brute Force
def minimumCostOfBreaking(X, Y, M, N):
    X.sort(reverse=True)
    Y.sort(reverse=True)
    hzntl, vert = 1, 1
    i, j, res = 0, 0, 0
    while i < M - 1 and j < N - 1:
        if X[i] > Y[j]:
            res += X[i] * vert
            hzntl += 1; i += 1
        else:
            res += Y[j] * hzntl
            vert += 1; j += 1
    while i < M - 1:
        res += X[i] * vert; i += 1
    while j < N - 1:
        res += Y[j] * hzntl; j += 1
    return res

# Time Complexity: O(M log M + N log N)
# Space Complexity: O(1)
# Explanation: Optimal: Sort all vertical and horizontal cuts in descending order. Maintain counts of horizontal and vertical pieces. Greedily pick the cut with the highest cost. If a horizontal cut is made, its total cost is `cut_cost * vertical_pieces`. Update the counts.

def minimumCostOfBreaking(X, Y, M, N):
    X.sort(reverse=True)
    Y.sort(reverse=True)
    hzntl, vert = 1, 1
    i, j, res = 0, 0, 0
    while i < M - 1 and j < N - 1:
        if X[i] > Y[j]:
            res += X[i] * vert
            hzntl += 1; i += 1
        else:
            res += Y[j] * hzntl
            vert += 1; j += 1
    while i < M - 1:
        res += X[i] * vert; i += 1
    while j < N - 1:
        res += Y[j] * hzntl; j += 1
    return res

