# Time Complexity: O(N * 2^N)
# Space Complexity: O(N)
# Explanation: Iterate through the string. If a prefix is a palindrome, add it to the current partition list, and recursively partition the remaining substring. When we reach the end of the string, add the current partition to the result.

def partition(s: str) -> List[List[str]]:
    def is_palindrome(sub):
        return sub == sub[::-1]
    res = []
    def solve(idx, path):
        if idx == len(s):
            res.append(path[:])
            return
        for i in range(idx, len(s)):
            if is_palindrome(s[idx:i+1]):
                path.append(s[idx:i+1])
                solve(i+1, path)
                path.pop()
    solve(0, [])
    return res

