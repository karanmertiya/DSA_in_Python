# Time Complexity: O(N! * N)
# Space Complexity: O(N)
# Explanation: Convert string to char array and sort it. Use backtracking: pass a boolean visited array and a temporary string. If temporary string length equals original length, add to answer. Else, iterate through characters. To avoid duplicates, if `i > 0` and `s[i] == s[i-1]` and `!vis[i-1]`, skip. Otherwise, mark visited, append, recurse, unmark, pop.

def find_permutation(S: str) -> List[str]:
    S = sorted(list(S))
    ans = []
    vis = [False] * len(S)
    def solve(curr):
        if len(curr) == len(S):
            ans.append("".join(curr))
            return
        for i in range(len(S)):
            if vis[i] or (i > 0 and S[i] == S[i-1] and not vis[i-1]):
                continue
            vis[i] = True
            curr.append(S[i])
            solve(curr)
            curr.pop()
            vis[i] = False
    solve([])
    return ans

