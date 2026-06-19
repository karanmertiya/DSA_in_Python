# Time Complexity: O(N<sup>2</sup>) (Trade-off)
# Space Complexity: O(N) (Trade-off)
# Explanation: Use two nested loops to count occurrences. Mark visited elements to avoid recounting.

def count_freq_brute(arr: list[int]) -> None:
    visited = [False] * len(arr)
    for i in range(len(arr)):
        if visited[i]: continue
        count = 1
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                visited[j] = True
                count += 1

