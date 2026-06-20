# Time Complexity: O(N^2) or worse
# Space Complexity: O(N) or O(1)
# Explanation: Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)

# TODO: Implement Brute Force
def maxProduct(arr, n):
    max_prod = float('-inf')
    pref, suff = 1, 1
    for i in range(n):
        if pref == 0: pref = 1
        if suff == 0: suff = 1
        pref *= arr[i]
        suff *= arr[n - i - 1]
        max_prod = max(max_prod, pref, suff)
    return max_prod

# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Optimal: Iterate from left to right calculating prefix product, and right to left calculating suffix product. If either is 0, reset it to 1. The max product will be the max of all prefix and suffix products.

def maxProduct(arr, n):
    max_prod = float('-inf')
    pref, suff = 1, 1
    for i in range(n):
        if pref == 0: pref = 1
        if suff == 0: suff = 1
        pref *= arr[i]
        suff *= arr[n - i - 1]
        max_prod = max(max_prod, pref, suff)
    return max_prod

