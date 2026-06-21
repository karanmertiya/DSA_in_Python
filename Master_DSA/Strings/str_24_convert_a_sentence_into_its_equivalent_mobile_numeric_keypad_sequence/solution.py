# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Store the sequence for every character in an array from A to Z, and for space. For each character in the input string, append its corresponding sequence to the result.

def printSequence(S):
    str_arr = ["2", "22", "222", "3", "33", "333", "4", "44", "444", "5", "55", "555", "6", "66", "666", "7", "77", "777", "7777", "8", "88", "888", "9", "99", "999", "9999"]
    output = ""
    for char in S:
        if char == ' ': output += "0"
        else: output += str_arr[ord(char) - ord('A')]
    return output

