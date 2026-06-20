# Time Complexity: O(N * 2^N)
# Space Complexity: O(N)
# Explanation: Iterate through the string. Extract substring `S[ind..i]`. If it is a palindrome, add it to the current partition list and recursively call for `i+1`. When `ind == length`, push the partition list to the answer.

def allPalindromicPerms(S: str) -> List[List[str]]:
    ans = []
    def is_pal(s): return s == s[::-1]
    def solve(ind, curr):
        if ind == len(S):
            ans.append(curr[:])
            return
        for i in range(ind, len(S)):
            sub = S[ind:i+1]
            if is_pal(sub):
                curr.append(sub)
                solve(i + 1, curr)
                curr.pop()
    solve(0, [])
    return ans

