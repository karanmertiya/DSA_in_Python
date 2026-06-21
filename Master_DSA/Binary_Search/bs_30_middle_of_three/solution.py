# Time Complexity: O(1)
# Space Complexity: O(1)
# Explanation: Optimal: Compare the numbers. If A is between B and C, return A. If B is between A and C, return B. Else return C.

def middle(A, B, C):
    if (A < B and B < C) or (C < B and B < A): return B
    if (B < A and A < C) or (C < A and A < B): return A
    return C

