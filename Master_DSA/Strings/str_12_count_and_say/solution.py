# Time Complexity: O(N * L) where L is max length of string
# Space Complexity: O(L)
# Explanation: Start with `res = '1'`. For `n-1` times, iterate through `res` and count consecutive identical characters. Append the count and the character to a new string. Replace `res` with the new string.

def countAndSay(n: int) -> str:
    if n == 1: return "1"
    s = "1"
    for _ in range(2, n + 1):
        temp = ""
        count = 1
        for j in range(1, len(s)):
            if s[j] == s[j - 1]:
                count += 1
            else:
                temp += str(count) + s[j - 1]
                count = 1
        temp += str(count) + s[-1]
        s = temp
    return s

