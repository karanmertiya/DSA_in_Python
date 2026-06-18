# Time Complexity: O(2<sup>N</sup>) (Constraint)
# Space Complexity: O(N) (Constraint)
# Explanation: Pick / Non-Pick logic. For every element, we have two choices: either include it in the current subset, or don't. Recursively explore both paths.

def subsets(nums: list[int]) -> list[list[int]]:
    ans = []
    def solve(i, temp):
        if i == len(nums):
            ans.append(temp.copy())
            return
        # Pick
        temp.append(nums[i])
        solve(i + 1, temp)
        temp.pop()
        
        # Not Pick
        solve(i + 1, temp)
        
    solve(0, [])
    return ans

