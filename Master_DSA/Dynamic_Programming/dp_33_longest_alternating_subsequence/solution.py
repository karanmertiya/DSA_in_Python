# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Maintain two lengths: `up` (ending with ascending) and `down` (ending with descending). Iterate array: if `arr[i] > arr[i-1]`, `up = down + 1`. If `arr[i] < arr[i-1]`, `down = up + 1`. Return `max(up, down)`.

def AlternatingaMaxLength(nums: List[int]) -> int:
    if not nums: return 0
    up = down = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]: up = down + 1
        elif nums[i] < nums[i-1]: down = up + 1
    return max(up, down)

