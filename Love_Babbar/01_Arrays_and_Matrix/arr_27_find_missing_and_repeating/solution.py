# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Optimal: Mathematical approach. Diff = Sum_N - Sum_Arr = Missing - Repeating. SumSqDiff = SumSq_N - SumSq_Arr = Missing^2 - Repeating^2. Use formulas to solve for both.

def findTwoElement(arr: List[int], n: int) -> List[int]:
    S_N = (n * (n+1)) // 2
    Sq_N = (n * (n+1) * (2*n+1)) // 6
    S, Sq = 0, 0
    for num in arr:
        S += num; Sq += num * num
    val1 = S_N - S # X - Y
    val2 = (Sq_N - Sq) // val1 # X + Y
    x = (val1 + val2) // 2
    y = x - val1
    return [y, x] # Repeating, Missing

