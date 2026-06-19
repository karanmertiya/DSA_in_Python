# Time Complexity: O(N * max_len)
# Space Complexity: O(max_len)
# Explanation: Start with "1". For `n-1` times, generate the next string by counting consecutive identical characters and appending `count` followed by the `character`.

def countAndSay(n):
    if n == 1: return "1"
    s = countAndSay(n - 1)
    res, count = "", 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]: count += 1
        else:
            res += str(count) + s[i-1]
            count = 1
    res += str(count) + s[-1]
    return res

