# Time Complexity: O(N log N)
# Space Complexity: O(1)
# Explanation: Sort arrival and departure arrays separately. Use two pointers, one for arrival and one for departure. If arrival < departure, a platform is needed, so increment count. If arrival >= departure, a platform is freed, so decrement count. Track the maximum count.

def findPlatform(arr, dep, n):
    arr.sort()
    dep.sort()
    plat_needed, result = 1, 1
    i, j = 1, 0
    while i < n and j < n:
        if arr[i] <= dep[j]:
            plat_needed += 1
            i += 1
        else:
            plat_needed -= 1
            j += 1
        result = max(result, plat_needed)
    return result

