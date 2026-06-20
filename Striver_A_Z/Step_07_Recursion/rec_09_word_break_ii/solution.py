# Time Complexity: O(2^N)
# Space Complexity: O(2^N)
# Explanation: Backtracking. Generate all combinations. At each step, if a prefix is in dict, recursively call for the rest of the string and append the prefix to the result of the recursive call.

def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    word_set = set(wordDict)
    memo = {}
    def solve(s):
        if s in memo: return memo[s]
        if not s: return [""]
        res = []
        for i in range(1, len(s) + 1):
            word = s[:i]
            if word in word_set:
                rem = solve(s[i:])
                for st in rem:
                    res.append(word + (" " if st else "") + st)
        memo[s] = res
        return res
    return solve(s)

