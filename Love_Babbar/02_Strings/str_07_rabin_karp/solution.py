# Time Complexity: O(N + M)
# Space Complexity: O(1)
# Explanation: Compute hash for pattern and first window of text. Slide window: subtract leading char's hash contribution, shift, and add trailing char. If hashes match, explicitly check strings to avoid collisions.

def search(pat: str, txt: str) -> List[int]:
    d, q = 256, 101
    m, n = len(pat), len(txt)
    if m > n: return []
    res, p, t, h = [], 0, 0, 1
    for i in range(m-1): h = (h * d) % q
    for i in range(m):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q
    for i in range(n - m + 1):
        if p == t:
            if txt[i:i+m] == pat:
                res.append(i + 1)
        if i < n - m:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i+m])) % q
            if t < 0: t += q
    return res

