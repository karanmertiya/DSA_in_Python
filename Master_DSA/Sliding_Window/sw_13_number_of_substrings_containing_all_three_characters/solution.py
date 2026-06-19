# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Iterate through the string. Track the last seen indices of 'a', 'b', and 'c'. If all three have been seen, the number of valid substrings ending at the current index `i` is `1 + min(last_a, last_b, last_c)`. Add this to the total count.

def numberOfSubstrings(s):
    last = [-1, -1, -1]
    count = 0
    for i in range(len(s)):
        last[ord(s[i]) - ord('a')] = i
        if last[0] != -1 and last[1] != -1 and last[2] != -1:
            count += 1 + min(last)
    return count

