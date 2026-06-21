# Time Complexity: O(log10 N)
# Space Complexity: O(log10 N)
# Explanation: Convert the absolute value of the number to a string and return its length.

def countDigits(n: int) -> int:
    return len(str(abs(n)))

# Time Complexity: O(log10 N)
# Space Complexity: O(1)
# Explanation: Use a while loop to repeatedly divide the number by 10 and increment a counter.

def countDigits(n: int) -> int:
    if n == 0: return 1
    count = 0
    # Use int(n/10) to truncate toward zero in Python
    while n != 0:
        count += 1
        n = int(n / 10)
    return count

# Time Complexity: O(log10 N)
# Space Complexity: O(1)
# Explanation: Use the base-10 logarithm function to find the number of digits mathematically.

import math
def countDigits(n: int) -> int:
    if n == 0: return 1
    return int(math.log10(abs(n)) + 1)

