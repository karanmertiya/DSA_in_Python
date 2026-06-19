# Time Complexity: O(2^N * N)
# Space Complexity: O(2^N * N)
# Explanation: Iterate from 1 to `2^N - 1`. For each number, treat its binary representation as a mask to pick characters from the string. Sort the resulting list of subsequences.

def AllPossibleStrings(s):
    n = len(s)
    ans = []
    for i in range(1, 1 << n):
        sub = ""
        for j in range(n):
            if i & (1 << j):
                sub += s[j]
        ans.append(sub)
    ans.sort()
    return ans

