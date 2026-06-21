# Time Complexity: O(N^2)
# Space Complexity: O(N)
# Explanation: Compute LIS ending at `i` from left to right (`inc[i]`). Compute LIS starting at `i` from right to left (`dec[i]`). The max bitonic subsequence length is `max(inc[i] + dec[i] - 1)` for all `i`. Sometimes pure increasing or pure decreasing is also bitonic depending on definition, adjust if necessary.

def LongestBitonicSequence(nums: List[int]) -> int:
    n = len(nums)
    inc = [1] * n
    dec = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]: inc[i] = max(inc[i], inc[j] + 1)
    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i, -1):
            if nums[i] > nums[j]: dec[i] = max(dec[i], dec[j] + 1)
    return max(inc[i] + dec[i] - 1 for i in range(n))

