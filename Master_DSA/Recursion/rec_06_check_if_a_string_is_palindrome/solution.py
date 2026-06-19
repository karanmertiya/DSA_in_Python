# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Check if `S[l] == S[r]`. If yes, recursively check `isPalindrome(S, l+1, r-1)`. Base case: `l >= r` returns true.

def isPalindrome(S):
    def isPal(l, r):
        if l >= r: return 1
        if S[l] != S[r]: return 0
        return isPal(l + 1, r - 1)
    return isPal(0, len(S) - 1)

