# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: If lengths don't match, return false. Use three pointers `i`, `j`, `k` for `str1`, `str2`, and `str3`. Traverse `str3`. If `str3[k] == str1[i]`, increment `i` and `k`. Else if `str3[k] == str2[j]`, increment `j` and `k`. Else, it's not a valid shuffle. After the loop, check if both `str1` and `str2` are fully traversed.

def checkShuffle(str1: str, str2: str, str3: str) -> bool:
    if len(str1) + len(str2) != len(str3): return False
    i, j, k = 0, 0, 0
    while k < len(str3):
        if i < len(str1) and str1[i] == str3[k]: i += 1
        elif j < len(str2) and str2[j] == str3[k]: j += 1
        else: return False
        k += 1
    return i == len(str1) and j == len(str2)

