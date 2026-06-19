# Time Complexity: O(N * 2^N)
# Space Complexity: O(2^N * N)
# Explanation: Backtracking. For each index, try all possible prefixes. If prefix is in dict, recursively break the remaining string. Use memoization or DP to store answers for a substring to avoid recomputation.

def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    wordSet = set(wordDict)
    memo = {}
    def dfs(s):
        if s in memo: return memo[s]
        res = []
        if s in wordSet: res.append(s)
        for i in range(1, len(s)):
            right = s[i:]
            if right in wordSet:
                left_res = dfs(s[:i])
                for l in left_res:
                    res.append(l + " " + right)
        memo[s] = res
        return res
    return dfs(s)

