# Time Complexity: O(N! * N)
# Space Complexity: O(N!)
# Explanation: Iterate from index `i` to `n-1`. Swap `str[i]` with `str[j]`, then recursively call for the next index. After returning, swap back to backtrack. Store permutations in a set or sort the array to handle duplicates and lexicographical order.

def find_permutation(S):
    st = set()
    S = list(S)
    def solve(idx):
        if idx == len(S):
            st.add("".join(S))
            return
        for i in range(idx, len(S)):
            S[idx], S[i] = S[i], S[idx]
            solve(idx + 1)
            S[idx], S[i] = S[i], S[idx]
    solve(0)
    return sorted(list(st))

