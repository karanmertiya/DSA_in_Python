# Time Complexity: O(N^3)
# Space Complexity: O(1) auxiliary
# Explanation: Sort array. Use 2 nested loops (i, j) for the first two numbers, and Two Pointers (k, l) for the remaining two. Skip duplicates carefully.

def fourSum(nums: List[int], target: int) -> List[List[int]]:
    ans = []
    n = len(nums); nums.sort()
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]: continue
        for j in range(i+1, n):
            if j > i+1 and nums[j] == nums[j-1]: continue
            k, l = j+1, n-1
            while k < l:
                total = nums[i] + nums[j] + nums[k] + nums[l]
                if total == target:
                    ans.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1; l -= 1
                    while k < l and nums[k] == nums[k-1]: k += 1
                    while k < l and nums[l] == nums[l+1]: l -= 1
                elif total < target: k += 1
                else: l -= 1
    return ans

