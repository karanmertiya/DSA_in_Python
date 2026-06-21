# Time Complexity: O(4^N * N)
# Space Complexity: O(N)
# Explanation: Backtracking. Create a mapping of digit to letters. Iterate through digits, for each digit loop through its mapped letters, append to current string, and recurse.

def letterCombinations(digits: str) -> List[str]:
    if not digits: return []
    ans = []
    mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    def solve(ind, path):
        if ind == len(digits):
            ans.append(path)
            return
        number = int(digits[ind])
        value = mapping[number]
        for i in range(len(value)):
            solve(ind + 1, path + value[i])
    solve(0, "")
    return ans

