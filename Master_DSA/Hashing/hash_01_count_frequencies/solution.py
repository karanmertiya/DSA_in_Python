# Time Complexity: O(N^2)
# Space Complexity: O(N)
# Explanation: Brute Force: Use two nested loops to count frequency of each element, marking visited ones.

def countFreq(arr):
    n = len(arr)
    visited = [False] * n
    for i in range(n):
        if visited[i]: continue
        count = 1
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                visited[j] = True
                count += 1
        print(arr[i], count)

# Time Complexity: O(N<sup>2</sup>) (Trade-off)
# Space Complexity: O(N) (Trade-off)
# Explanation: Optimal: Use two nested loops to count occurrences. Mark visited elements to avoid recounting.

def count_freq(arr: list[int]) -> None:\n    freq = {}\n    for num in arr:\n        freq[num] = freq.get(num, 0) + 1\n    for key, val in freq.items():\n        print(f'{key} {val}')

