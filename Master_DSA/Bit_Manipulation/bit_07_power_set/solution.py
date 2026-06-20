# Time Complexity: O(N * 2^N)
# Space Complexity: O(N * 2^N)
# Explanation: Bit manipulation technique. For N elements, there are 2^N subsets. Count from 0 to 2^N - 1. For each number, its binary representation indicates which elements to include.

def subsets(nums: List[int]) -> List[List[int]]:
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

