# Time Complexity: O(N * 2^N)
# Space Complexity: O(N * X)
# Explanation: Recurse through string. For index `i`, check substring `s[index...i]`. If it is palindrome, add it to current list, and recurse for `i+1`. Backtrack after recursion.

def partition(s: str) -> List[List[str]]:
    res = []
    def isPal(string, l, r):
        while l <= r:
            if string[l] != string[r]: return False
            l += 1; r -= 1
        return True
    def func(index, path):
        if index == len(s):
            res.append(list(path))
            return
        for i in range(index, len(s)):
            if isPal(s, index, i):
                path.append(s[index:i+1])
                func(i + 1, path)
                path.pop()
    func(0, [])
    return res

