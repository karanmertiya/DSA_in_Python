# Time Complexity: O(N^2) or worse
# Space Complexity: O(N) or O(1)
# Explanation: Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)

# TODO: Implement Brute Force
def leaders(A: List[int], N: int) -> List[int]:
    ans = []
    maxi = A[N - 1]
    ans.append(maxi)
    for i in range(N - 2, -1, -1):
        if A[i] >= maxi:
            ans.append(A[i])
            maxi = A[i]
    ans.reverse()
    return ans

# Time Complexity: O(N)
# Space Complexity: O(N) for output
# Explanation: Optimal: Traverse the array from right to left. Keep track of the maximum element seen so far. If the current element is greater than or equal to the max, it's a leader. Reverse the collected leaders at the end.

def leaders(A: List[int], N: int) -> List[int]:
    ans = []
    maxi = A[N - 1]
    ans.append(maxi)
    for i in range(N - 2, -1, -1):
        if A[i] >= maxi:
            ans.append(A[i])
            maxi = A[i]
    ans.reverse()
    return ans

