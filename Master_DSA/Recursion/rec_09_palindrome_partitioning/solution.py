# Time Complexity: O(N * 2^N)
# Space Complexity: O(N)
# Explanation: Backtracking. Try to partition the string at every index. If the prefix `s[start:i]` is a palindrome, add it to current path and recurse for the rest of the string `s[i:end]`.

def partition(s: str) -> List[List[str]]:
    res = []
    path = []
    def isPalindrome(s, start, end):
        while start <= end:
            if s[start] != s[end]: return False
            start += 1; end -= 1
        return True
    def solve(index):
        if index == len(s):
            res.append(list(path))
            return
        for i in range(index, len(s)):
            if isPalindrome(s, index, i):
                path.append(s[index:i+1])
                solve(i + 1)
                path.pop()
    solve(0)
    return res

