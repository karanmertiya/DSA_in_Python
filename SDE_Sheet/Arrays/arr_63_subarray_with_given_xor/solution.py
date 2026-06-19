# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Maintain the prefix XOR. Use a hash map to store the frequency of each prefix XOR. If current prefix XOR is `xr`, we want to find if there was a previous prefix XOR `xr ^ B`. If so, add its frequency to the count. Then add the current `xr` to the map.

def solve(A, B):
    freq = {}
    count = 0
    xr = 0
    for num in A:
        xr ^= num
        if xr == B: count += 1
        if (xr ^ B) in freq:
            count += freq[xr ^ B]
        freq[xr] = freq.get(xr, 0) + 1
    return count

