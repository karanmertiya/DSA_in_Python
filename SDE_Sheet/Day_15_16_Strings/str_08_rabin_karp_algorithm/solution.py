# Time Complexity: O(N + M)
# Space Complexity: O(1)
# Explanation: Compute the hash for the pattern and for the first window of text. Slide the window by removing the leading character's hash and adding the trailing character's hash. If hashes match, check the characters one by one.

def search(pat, txt):
    d, q = 256, 101
    M, N = len(pat), len(txt)
    p, t, h = 0, 0, 1
    res = []
    for i in range(M - 1): h = (h * d) % q
    for i in range(M):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q
    for i in range(N - M + 1):
        if p == t:
            match = True
            for j in range(M):
                if txt[i + j] != pat[j]:
                    match = False
                    break
            if match: res.append(i + 1)
        if i < N - M:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q
            if t < 0: t = t + q
    return res

