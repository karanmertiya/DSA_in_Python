# Time Complexity: O(2<sup>T</sup>) (Trade-off)
# Space Complexity: O(T) (Trade-off)
# Explanation: Pick/Non-Pick but when picking, we *do not* increment the index `i`, allowing the same element to be picked infinitely until `target < 0`.

def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    ans = []
    def solve(i, current_target, temp):
        if i == len(candidates):
            if current_target == 0:
                ans.append(temp.copy())
            return
            
        if candidates[i] <= current_target:
            temp.append(candidates[i])
            solve(i, current_target - candidates[i], temp)
            temp.pop()
            
        solve(i + 1, current_target, temp)
        
    solve(0, target, [])
    return ans

