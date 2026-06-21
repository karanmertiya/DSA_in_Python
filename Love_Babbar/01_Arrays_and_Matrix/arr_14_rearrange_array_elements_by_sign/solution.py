# Time Complexity: O(N) (Constraint)
# Space Complexity: O(N) (Constraint)
# Explanation: Optimal: Use two pointers, `pos_idx` starting at 0, `neg_idx` starting at 1. Traverse and place elements directly into a new result array.

def rearrangeArray(nums: list[int]) -> list[int]:
    ans = [0] * len(nums)
    pos_idx, neg_idx = 0, 1
    for num in nums:
        if num > 0:
            ans[pos_idx] = num
            pos_idx += 2
        else:
            ans[neg_idx] = num
            neg_idx += 2
    return ans

