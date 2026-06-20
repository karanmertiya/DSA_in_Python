# Time Complexity: O(N * d)
# Space Complexity: O(1)
# Explanation: Iterate through each number in the array. For each number, reverse its digits to check if it's a palindrome. If any number is not, return 0. If all are, return 1.

def PalinArray(arr, n):
    for num in arr:
        if str(num) != str(num)[::-1]:
            return 0
    return 1

