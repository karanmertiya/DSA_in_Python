# Time Complexity: O(N * 2^N)
# Space Complexity: O(N * 2^N)
# Explanation: Iterate from 1 to `(1 << n) - 1`. For each number, its binary representation indicates which characters of the string to include. Example: 011 means include 1st and 2nd char.

def AllPossibleStrings(s: str) -> List[str]:
    n = len(s)
    res = []
    for i in range(1, 1 << n):
        sub = ""
        for j in range(n):
            if i & (1 << j):
                sub += s[j]
        res.append(sub)
    res.sort()
    return res

