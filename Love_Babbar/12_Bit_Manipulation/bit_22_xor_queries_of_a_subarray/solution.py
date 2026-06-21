# Time Complexity: O(N + Q)
# Space Complexity: O(N)
# Explanation: Create a prefix XOR array. Query answer for `[L, R]` is `prefix[R] ^ prefix[L-1]`. If `L == 0`, answer is `prefix[R]`.

def xorQueries(arr: list[int], queries: list[list[int]]) -> list[int]:
    pref = [0] * len(arr)
    pref[0] = arr[0]
    for i in range(1, len(arr)):
        pref[i] = pref[i-1] ^ arr[i]
    ans = []
    for l, r in queries:
        if l == 0: ans.append(pref[r])
        else: ans.append(pref[r] ^ pref[l-1])
    return ans

