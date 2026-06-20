# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Map each Roman numeral to its integer value. Iterate from right to left. If a character is smaller than its right character, subtract its value, else add it.

def romanToDecimal(S):
    m = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0
    for i in range(len(S)):
        if i + 1 < len(S) and m[S[i]] < m[S[i+1]]:
            ans -= m[S[i]]
        else:
            ans += m[S[i]]
    return ans

