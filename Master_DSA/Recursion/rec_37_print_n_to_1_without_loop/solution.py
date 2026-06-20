# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Use a recursive function. Print `N` first and then call `f(N-1)`.

def printNos(N):
    if N == 0: return
    print(N, end=" ")
    printNos(N - 1)

