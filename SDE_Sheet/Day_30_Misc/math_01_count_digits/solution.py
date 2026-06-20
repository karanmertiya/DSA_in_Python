# Time Complexity: O(1)
# Space Complexity: O(1)
# Explanation: Convert the number to a string and return its length.

def countDigits(n: int) -> int:
    return len(str(n))

# Time Complexity: O(log10 N)
# Space Complexity: O(1)
# Explanation: Use a while loop to repeatedly divide the number by 10 and increment a counter.

def countDigits(n: int) -> int:
    if n == 0: return 1
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

# Time Complexity: O(1)
# Space Complexity: O(1)
# Explanation: Use the base-10 logarithm function to find the number of digits mathematically.

import math
def countDigits(n: int) -> int:
    if n == 0: return 1
    return int(math.log10(n) + 1)

