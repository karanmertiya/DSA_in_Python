# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Since `pref[i] = pref[i-1] ^ arr[i]`, we can find `arr[i]` by doing `pref[i-1] ^ pref[i]`. `arr[0] = pref[0]`.

def findArray(pref: list[int]) -> list[int]:
    arr = [0] * len(pref)
    arr[0] = pref[0]
    for i in range(1, len(pref)):
        arr[i] = pref[i-1] ^ pref[i]
    return arr

