# Time Complexity: O(N^2) or worse
# Space Complexity: O(N) or O(1)
# Explanation: Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)

# TODO: Implement Brute Force
def commonElements(A: List[int], B: List[int], C: List[int], n1: int, n2: int, n3: int) -> List[int]:
    res = []
    i = j = k = 0
    while i < n1 and j < n2 and k < n3:
        if A[i] == B[j] == C[k]:
            if not res or res[-1] != A[i]:
                res.append(A[i])
            i += 1; j += 1; k += 1
        elif A[i] <= B[j] and A[i] <= C[k]: i += 1
        elif B[j] <= A[i] and B[j] <= C[k]: j += 1
        else: k += 1
    return res

# Time Complexity: O(N1 + N2 + N3)
# Space Complexity: O(1)
# Explanation: Optimal: Use three pointers `i`, `j`, `k` for the three arrays. If `A[i] == B[j] == C[k]`, it's a common element, add it to the result (handling duplicates), and increment all three pointers. Else, increment the pointer that points to the smallest value.

def commonElements(A: List[int], B: List[int], C: List[int], n1: int, n2: int, n3: int) -> List[int]:
    res = []
    i = j = k = 0
    while i < n1 and j < n2 and k < n3:
        if A[i] == B[j] == C[k]:
            if not res or res[-1] != A[i]:
                res.append(A[i])
            i += 1; j += 1; k += 1
        elif A[i] <= B[j] and A[i] <= C[k]: i += 1
        elif B[j] <= A[i] and B[j] <= C[k]: j += 1
        else: k += 1
    return res

