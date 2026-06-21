# Time Complexity: O(2^N)
# Space Complexity: O(N)
# Explanation: First find the number of misplaced left (`rm_l`) and right (`rm_r`) parentheses. Then use backtracking to try removing `rm_l` and `rm_r` parentheses. To avoid duplicates, skip identical adjacent characters. Finally, check if the resulting string is valid.

def removeInvalidParentheses(s: str) -> List[str]:
    def is_valid(s):
        count = 0
        for c in s:
            if c == '(': count += 1
            elif c == ')': count -= 1
            if count < 0: return False
        return count == 0
    rm_l, rm_r = 0, 0
    for c in s:
        if c == '(': rm_l += 1
        elif c == ')':
            if rm_l > 0: rm_l -= 1
            else: rm_r += 1
    ans = []
    def solve(s, start, rm_l, rm_r):
        if rm_l == 0 and rm_r == 0:
            if is_valid(s): ans.append(s)
            return
        for i in range(start, len(s)):
            if i != start and s[i] == s[i-1]: continue
            if s[i] == '(' and rm_l > 0:
                solve(s[:i] + s[i+1:], i, rm_l - 1, rm_r)
            elif s[i] == ')' and rm_r > 0:
                solve(s[:i] + s[i+1:], i, rm_l, rm_r - 1)
    solve(s, 0, rm_l, rm_r)
    return ans

