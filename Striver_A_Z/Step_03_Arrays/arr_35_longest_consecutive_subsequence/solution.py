# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Insert all elements into a hash set. For each element, check if `element - 1` exists. If not, it's the start of a sequence. Then increment to find consecutive elements.

def findLongestConseqSubseq(arr, N):
    s = set(arr)
    longest = 0
    for num in s:
        if (num - 1) not in s:
            curr = num
            count = 1
            while (curr + 1) in s:
                curr += 1
                count += 1
            longest = max(longest, count)
    return longest

