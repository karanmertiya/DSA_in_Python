# Time Complexity: O(2^N * K)
# Space Complexity: O(K * X)
# Explanation: Sort the array and remove duplicates. Use backtracking. At each step, either include the current element (and stay at the current element to allow unlimited picks) or move to the next element. Backtrack when sum < 0 or we reach the end.

def combinationSum(A, B):
    A = sorted(list(set(A)))
    ans = []
    def solve(idx, current_sum, curr):
        if current_sum == B:
            ans.append(list(curr))
            return
        if current_sum > B or idx == len(A): return
        curr.append(A[idx])
        solve(idx, current_sum + A[idx], curr)
        curr.pop()
        solve(idx + 1, current_sum, curr)
    solve(0, 0, [])
    return ans

