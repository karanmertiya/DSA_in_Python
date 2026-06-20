# Time Complexity: O(N^2) or worse
# Space Complexity: O(N) or O(1)
# Explanation: Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)

# TODO: Implement Brute Force
def solve(A: List[int], B: int) -> int:
    mpp = {0: 1}
    xr = count = 0
    for num in A:
        xr ^= num
        x = xr ^ B
        if x in mpp: count += mpp[x]
        mpp[xr] = mpp.get(xr, 0) + 1
    return count

# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Optimal: Use a Hash Map to store the frequency of prefix XORs. For each element, current XOR `xr ^= A[i]`. We need `xr ^ B`. If it exists in map, add its frequency to count.

def solve(A: List[int], B: int) -> int:
    mpp = {0: 1}
    xr = count = 0
    for num in A:
        xr ^= num
        x = xr ^ B
        if x in mpp: count += mpp[x]
        mpp[xr] = mpp.get(xr, 0) + 1
    return count

