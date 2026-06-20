# Time Complexity: O(2^N)
# Space Complexity: O(N)
# Explanation: Iterate from current index. For each prefix, if it is in the dictionary, add it to the current sentence string, add a space, and recur for the suffix. If we reach the end of the string, add the current sentence to the answer.

def wordBreak(n, dict_words, s):
    st = set(dict_words)
    ans = []
    def solve(idx, curr):
        if idx == len(s):
            ans.append(curr.strip())
            return
        for i in range(idx, len(s)):
            word = s[idx:i+1]
            if word in st:
                solve(i + 1, curr + word + " ")
    solve(0, "")
    return ans

