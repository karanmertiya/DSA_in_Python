# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Calculate the sum of first N natural numbers using `N*(N+1)/2`. Subtract the sum of all elements in the array from it. The result is the missing number.

def missingNumber(array, n):
    return n * (n + 1) // 2 - sum(array)

