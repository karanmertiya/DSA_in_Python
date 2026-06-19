# Time Complexity: O(2<sup>N</sup> * N)
# Space Complexity: O(N)
# Explanation: Pick / Not Pick technique. For every element, branch recursively: one path includes the element, the other path excludes it.

def subsets(nums: list[int]) -> list[list[int]]:
    ans = []
    def solve(idx, temp):
        if idx == len(nums):
            ans.append(temp[:])
            return
        temp.append(nums[idx])
        solve(idx + 1, temp)
        temp.pop()
        solve(idx + 1, temp)
    solve(0, [])
    return ans

