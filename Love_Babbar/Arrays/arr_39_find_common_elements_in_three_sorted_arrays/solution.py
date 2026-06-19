# Time Complexity: O(N1 + N2 + N3)
# Space Complexity: O(1) extra space
# Explanation: Maintain three pointers `i`, `j`, `k` for the three arrays. If `A[i] == B[j] == C[k]`, add to result and increment all three. Otherwise, increment the pointer of the smallest element. Skip duplicates.

def commonElements(A, B, C, n1, n2, n3):
    i, j, k = 0, 0, 0
    res = []
    while i < n1 and j < n2 and k < n3:
        if A[i] == B[j] and B[j] == C[k]:
            if not res or res[-1] != A[i]:
                res.append(A[i])
            i += 1; j += 1; k += 1
        elif A[i] < B[j]: i += 1
        elif B[j] < C[k]: j += 1
        else: k += 1
    return res

