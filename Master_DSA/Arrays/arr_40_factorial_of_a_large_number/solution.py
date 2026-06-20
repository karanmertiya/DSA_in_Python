# Time Complexity: O(N^2) or worse
# Space Complexity: O(N) or O(1)
# Explanation: Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)

# TODO: Implement Brute Force
def factorial(N):
    # Python handles large integers automatically
    import math
    fact = math.factorial(N)
    return [int(x) for x in str(fact)]

# Time Complexity: O(N^2)
# Space Complexity: O(N log(N!))
# Explanation: Optimal: Use an array to store the result. Initially, it holds 1. Multiply the array by numbers from 2 to N. The multiplication is done school-style by carrying over remainders to the next index.

def factorial(N):
    # Python handles large integers automatically
    import math
    fact = math.factorial(N)
    return [int(x) for x in str(fact)]

