# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Use a recursive function. Call `f(N-1)` first and then print `N`.

def printTillN(N):
    if N == 0: return
    printTillN(N - 1)
    print(N, end=" ")

