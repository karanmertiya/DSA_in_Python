# Time Complexity: O(2^N * N)
# Space Complexity: O(N)
# Explanation: Iterate over the string to pick substrings. Check if the picked substring is a palindrome. If yes, add it to current partition and recur for the remaining string. Backtrack by removing it.

def isPalindrome(s, l, r):
    while l < r:
        if s[l] != s[r]: return False
        l += 1; r -= 1
    return True

def allPalindromicPerms(S):
    ans, curr = [], []
    def solve(idx):
        if idx == len(S):
            ans.append(list(curr))
            return
        for i in range(idx, len(S)):
            if isPalindrome(S, idx, i):
                curr.append(S[idx:i+1])
                solve(i + 1)
                curr.pop()
    solve(0)
    return ans

