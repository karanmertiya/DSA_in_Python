# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: The maximum possible value is `(1 << maximumBit) - 1`. If current running XOR is `curr`, we want `k` such that `curr ^ k = max_val`. Thus `k = curr ^ max_val`. Do this iteratively backwards.

def getMaximumXor(nums: List[int], maximumBit: int) -> List[int]:
    curr = 0
    for n in nums: curr ^= n
    max_val = (1 << maximumBit) - 1
    ans = []
    for i in range(len(nums)-1, -1, -1):
        ans.append(curr ^ max_val)
        curr ^= nums[i]
    return ans

