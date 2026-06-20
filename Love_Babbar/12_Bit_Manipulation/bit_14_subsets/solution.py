# Time Complexity: O(N * 2^N)
# Space Complexity: O(N * 2^N)
# Explanation: Recursive backtracking (include/exclude pattern).

def subsets_rec(nums: list[int]) -> list[list[int]]:
    ans, curr = [], []
    def solve(idx):
        if idx == len(nums):
            ans.append(curr[:])
            return
        curr.append(nums[idx])
        solve(idx + 1)
        curr.pop()
        solve(idx + 1)
    solve(0)
    return ans

# Time Complexity: O(N * 2^N)
# Space Complexity: O(N * 2^N)
# Explanation: Bit manipulation technique. For N elements, there are 2^N subsets. Count from 0 to 2^N - 1. For each number, its binary representation indicates which elements to include.

def subsets(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    subsets_count = 1 << n
    ans = []
    for i in range(subsets_count):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(nums[j])
        ans.append(subset)
    return ans

