# Time Complexity: O(N + M)
# Space Complexity: O(M)
# Explanation: Construct an LPS (Longest Proper Prefix which is also Suffix) array for the pattern. Use it to skip unnecessary comparisons while traversing the text.

def computeLPS(pat, M, lps):
    length = 0
    lps[0] = 0
    i = 1
    while i < M:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

def search(pat, txt):
    M, N = len(pat), len(txt)
    lps = [0] * M
    computeLPS(pat, M, lps)
    i, j = 0, 0
    res = []
    while (N - i) >= (M - j):
        if pat[j] == txt[i]:
            j += 1; i += 1
        if j == M:
            res.append(i - j + 1)
            j = lps[j - 1]
        elif i < N and pat[j] != txt[i]:
            if j != 0: j = lps[j - 1]
            else: i += 1
    return res

