# Time Complexity: O(2^N)
# Space Complexity: O(N) recursion stack
# Explanation: Use recursion. At each character, you have two choices: either include it in the current subsequence or exclude it. When you reach the end of the string, print/store the formed subsequence.

def allSubsequences(s: str) -> List[str]:
    res = []
    def solve(i, curr):
        if i == len(s):
            if curr: res.append(curr)
            return
        solve(i + 1, curr)
        solve(i + 1, curr + s[i])
    solve(0, "")
    return res

