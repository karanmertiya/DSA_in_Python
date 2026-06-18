# Time Complexity: O(N) (Constraint)
# Space Complexity: O(N) (Trade-off)
# Explanation: Use an extra array to place elements at `(i + k) % N`.

def rotate_brute(nums: list[int], k: int) -> None:
    n = len(nums)
    k = k % n
    temp = [0] * n
    for i in range(n):
        temp[(i + k) % n] = nums[i]
    for i in range(n):
        nums[i] = temp[i]

# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1) (Constraint)
# Explanation: Reverse parts of the array: Reverse full array, reverse first `k`, reverse rest.

def rotate_optimal(nums: list[int], k: int) -> None:
    n = len(nums)
    k = k % n
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])

