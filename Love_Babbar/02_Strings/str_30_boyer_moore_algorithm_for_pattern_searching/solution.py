# Time Complexity: O(N * M)
# Space Complexity: O(256)
# Explanation: Create a Bad Character table for the pattern, which stores the last occurrence of each character. Align pattern with text. Compare from right to left. If mismatch, shift the pattern so that the mismatched character in text aligns with its last occurrence in the pattern. If not present, shift pattern past it.

def search(txt, pat):
    m, n = len(pat), len(txt)
    badChar = [-1] * 256
    for i in range(m): badChar[ord(pat[i])] = i
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pat[j] == txt[s + j]: j -= 1
        if j < 0:
            print(f"Pattern occurs at shift = {s}")
            s += (m - badChar[ord(txt[s + m])] if s + m < n else 1)
        else:
            s += max(1, j - badChar[ord(txt[s + j])])

