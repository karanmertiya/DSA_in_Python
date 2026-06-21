# Time Complexity: O(2^9)
# Space Complexity: O(k)
# Explanation: Backtracking. Start from 1, go up to 9. Add the current number to the path and subtract from target. Stop when path size is `k` and `target` is 0.

def combinationSum3(k: int, n: int) -> List[List[int]]:
    ans = []
    def solve(start, k, n, ds):
        if k == 0 and n == 0:
            ans.append(list(ds))
            return
        if k == 0 or n < 0: return
        for i in range(start, 10):
            ds.append(i)
            solve(i + 1, k - 1, n - i, ds)
            ds.pop()
    solve(1, k, n, [])
    return ans

