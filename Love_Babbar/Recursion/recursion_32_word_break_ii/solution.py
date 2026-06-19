# Time Complexity: O(N * 2^N)
# Space Complexity: O(N * 2^N)
# Explanation: Iterate through all possible prefixes. If a prefix exists in the wordDict, recursively solve for the remaining suffix. Backtrack by appending the current prefix to the results of the suffix.

def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    dict_set = set(wordDict)
    res = []
    def solve(idx, path):
        if idx == len(s):
            res.append(path[:-1])
            return
        temp = ""
        for i in range(idx, len(s)):
            temp += s[i]
            if temp in dict_set:
                solve(i + 1, path + temp + " ")
    solve(0, "")
    return res

