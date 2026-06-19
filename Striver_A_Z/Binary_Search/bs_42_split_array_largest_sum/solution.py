# Time Complexity: O(N log(sum - max))
# Space Complexity: O(1)
# Explanation: Binary search the max subarray sum `[max(nums), sum(nums)]`. For a `mid`, greedily split array. If subarrays needed `<= k`, `mid` is possible, search lower. Else search higher.

def splitArray(nums: List[int], k: int) -> int:
    low, high = max(nums), sum(nums)
    while low < high:
        mid = low + (high - low) // 2
        pieces, currentSum = 1, 0
        for n in nums:
            if currentSum + n > mid:
                currentSum = n
                pieces += 1
            else:
                currentSum += n
        if pieces <= k:
            high = mid
        else:
            low = mid + 1
    return low

