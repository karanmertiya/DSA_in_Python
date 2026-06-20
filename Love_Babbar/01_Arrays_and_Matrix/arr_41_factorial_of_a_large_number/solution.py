# Time Complexity: O(N^2)
# Space Complexity: O(N log(N!))
# Explanation: Use an array to store the result. Initially, it holds 1. Multiply the array by numbers from 2 to N. The multiplication is done school-style by carrying over remainders to the next index.

def factorial(N):
    # Python handles large integers automatically
    import math
    fact = math.factorial(N)
    return [int(x) for x in str(fact)]

