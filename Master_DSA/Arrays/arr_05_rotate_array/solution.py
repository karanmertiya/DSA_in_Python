# Time Complexity: O(N * K) or O(N)
# Space Complexity: O(1) or O(N)
# Explanation: Brute Force: Rotate the array one by one, k times. Or use a temporary array of size N.

def rotate(nums, k):
    n = len(nums)
    k = k % n
    temp = [0] * n
    for i in range(n):
        temp[(i+k)%n] = nums[i]
    for i in range(n):
        nums[i] = temp[i]

# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1) (Constraint)
# Explanation: Optimal: Reverse Algorithm. Reverse the whole array, then reverse the first `k` elements, then reverse the remaining `N-k` elements.

def rotate(nums: list[int], k: int) -> None:
    n = len(nums)
    k = k % n
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])

