# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: There are only two possible alternating strings for length N: starting with '0' (`010101...`) and starting with '1' (`101010...`). Count the differences between the given string and both of these. The minimum count is the answer.

def minFlips(S):
    count1, count2 = 0, 0
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i] != '0': count1 += 1
            if S[i] != '1': count2 += 1
        else:
            if S[i] != '1': count1 += 1
            if S[i] != '0': count2 += 1
    return min(count1, count2)

