# Time Complexity: O(N)
# Space Complexity: O(1) excluding output
# Explanation: Iterate from the end of the string. The first odd digit found marks the end of the largest odd integer (since picking all digits from index 0 to this odd digit yields the largest value). Return the substring `num[0..i]`. If no odd digit is found, return empty string.

def largestOddNumber(num):
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2 != 0: return num[:i+1]
    return ""

