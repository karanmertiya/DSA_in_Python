# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Use a Hash Map to count occurrences. Return the element with count 1.

from collections import Counter
def single_number_hash(nums: list[int]) -> int:
    counts = Counter(nums)
    for num, count in counts.items():
        if count == 1: return num
    return -1

# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Use XOR bitwise operation. `X ^ X = 0` and `X ^ 0 = X`. XORing all elements pairs up the duplicates to 0, leaving the single element.

def single_number(nums: list[int]) -> int:
    ans = 0
    for num in nums:
        ans ^= num
    return ans

