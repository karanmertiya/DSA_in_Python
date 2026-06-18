# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1)
# Explanation: Skip whitespaces, parse sign, and construct integer utilizing math bound checks before applying `x10`.

def my_atoi(s: str) -> int:
    s = s.lstrip()
    if not s: return 0
    sign = -1 if s[0] == '-' else 1
    if s[0] in ['-', '+']: s = s[1:]
    
    res = 0
    for char in s:
        if not char.isdigit(): break
        res = res * 10 + int(char)
        
    res = sign * res
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    if res < INT_MIN: return INT_MIN
    if res > INT_MAX: return INT_MAX
    return res

