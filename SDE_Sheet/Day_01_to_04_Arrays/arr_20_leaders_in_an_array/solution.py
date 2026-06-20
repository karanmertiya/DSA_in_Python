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

