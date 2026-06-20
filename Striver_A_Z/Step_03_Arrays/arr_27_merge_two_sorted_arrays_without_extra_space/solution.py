# Time Complexity: O(N^2) or worse
# Space Complexity: O(N) or O(1)
# Explanation: Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)

# TODO: Implement Brute Force
def merge(arr1: List[int], arr2: List[int], n: int, m: int) -> None:
    left, right = n - 1, 0
    while left >= 0 and right < m:
        if arr1[left] > arr2[right]:
            arr1[left], arr2[right] = arr2[right], arr1[left]
            left -= 1; right += 1
        else: break
    arr1.sort(); arr2.sort()

# Time Complexity: O((N+M) log(N+M))
# Space Complexity: O(1)
# Explanation: Optimal: Start pointers at end of arr1 (i) and beginning of arr2 (j). Swap if arr1[i] > arr2[j]. Afterwards, individually sort arr1 and arr2. Time is bounded by sorting.

def merge(arr1: List[int], arr2: List[int], n: int, m: int) -> None:
    left, right = n - 1, 0
    while left >= 0 and right < m:
        if arr1[left] > arr2[right]:
            arr1[left], arr2[right] = arr2[right], arr1[left]
            left -= 1; right += 1
        else: break
    arr1.sort(); arr2.sort()

