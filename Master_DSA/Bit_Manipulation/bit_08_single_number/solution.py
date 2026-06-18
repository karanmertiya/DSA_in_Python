# Time Complexity: O(N) (Constraint)
# Space Complexity: O(N) (Trade-off)
# Explanation: Use a Hash Map to count occurrences. Return the element with count 1.

def single_number_brute(nums: list[int]) -> int:
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    for num, count in freq.items():
        if count == 1:
            return num
    return -1

# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1) (Constraint)
# Explanation: XOR all elements. Identical pairs cancel out (A ^ A = 0), leaving only the unique element (0 ^ B = B).

def single_number_optimal(nums: list[int]) -> int:
    xor_res = 0
    for num in nums:
        xor_res ^= num
    return xor_res

