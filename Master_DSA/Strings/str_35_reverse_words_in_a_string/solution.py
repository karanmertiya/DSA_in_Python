# Time Complexity: O(N)
# Space Complexity: O(N) for output string
# Explanation: Iterate from right to left. Find the end of a word, then the start of a word. Extract the word and append it to the result string along with a space. Finally, remove the trailing space.

def reverseWords(s):
    return " ".join(s.split()[::-1])

