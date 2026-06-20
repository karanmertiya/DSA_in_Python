# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: 1. Ignore leading whitespaces. 2. Check for optional '+' or '-'. 3. Read digits until a non-digit or end of string. 4. Build the integer, checking for 32-bit integer overflow/underflow at each step.

def myAtoi(s):
    s = s.lstrip()
    if not s: return 0
    sign = -1 if s[0] == '-' else 1
    if s[0] in ['-', '+']: s = s[1:]
    ans = 0
    for c in s:
        if not c.isdigit(): break
        ans = ans * 10 + int(c)
    ans *= sign
    ans = max(-2**31, min(ans, 2**31 - 1))
    return ans

