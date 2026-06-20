# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Optimal: Iterate while counting 1s. If a 0 is found, update max count and reset current count to 0.

def findMaxConsecutiveOnes(nums: list[int]) -> int:
    max_cnt = current_cnt = 0
    for num in nums:
        if num == 1:
            current_cnt += 1
            max_cnt = max(max_cnt, current_cnt)
        else:
            current_cnt = 0
    return max_cnt

