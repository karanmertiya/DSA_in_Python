# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Maintain prefix XOR. Use hash map to store prefix XOR frequencies. If current XOR is `xr`, we need a previous XOR `xr ^ B`. Add its frequency to count. Insert `xr` to map.

def solve(A, B):
    m = {}
    xr, count = 0, 0
    for num in A:
        xr ^= num
        if xr == B: count += 1
        if xr ^ B in m:
            count += m[xr ^ B]
        m[xr] = m.get(xr, 0) + 1
    return count

