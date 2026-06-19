# Time Complexity: O(4^N)
# Space Complexity: O(N)
# Explanation: Iterate through the string, extracting substrings as numbers. Prevent numbers with leading zeros. Recursively try `+`, `-`, `*`. For `*`, we must subtract the previous added value, and add `prev * current_val` to maintain precedence.

def addOperators(num: str, target: int) -> List[str]:
    res = []
    def solve(idx, path, prevNum, currVal):
        if idx == len(num):
            if currVal == target: res.append(path)
            return
        s = ""
        n = 0
        for i in range(idx, len(num)):
            if i > idx and num[idx] == '0': break
            s += num[i]
            n = n * 10 + int(num[i])
            if idx == 0:
                solve(i + 1, s, n, n)
            else:
                solve(i + 1, path + "+" + s, n, currVal + n)
                solve(i + 1, path + "-" + s, -n, currVal - n)
                solve(i + 1, path + "*" + s, prevNum * n, currVal - prevNum + prevNum * n)
    solve(0, "", 0, 0)
    return res

