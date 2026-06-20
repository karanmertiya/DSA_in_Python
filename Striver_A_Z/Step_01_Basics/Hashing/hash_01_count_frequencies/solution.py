# Time Complexity: O(N<sup>2</sup>) (Trade-off)
# Space Complexity: O(N) (Trade-off)
# Explanation: Use two nested loops to count occurrences. Mark visited elements to avoid recounting.

def count_freq(arr: list[int]) -> None:\n    freq = {}\n    for num in arr:\n        freq[num] = freq.get(num, 0) + 1\n    for key, val in freq.items():\n        print(f'{key} {val}')

