# Time Complexity: O(N! * N)
# Space Complexity: O(N)
# Explanation: Backtracking. Swap elements to generate permutations. For index `i`, swap it with every index from `i` to `n-1`, recurse, then backtrack (swap back).

def permute(nums: list[int]) -> list[list[int]]:
    ans = []
    def solve(idx):
        if idx == len(nums):
            ans.append(nums[:])
            return
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            solve(idx + 1)
            nums[idx], nums[i] = nums[i], nums[idx]
    solve(0)
    return ans

