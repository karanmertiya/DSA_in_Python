# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1) (Constraint)
# Explanation: Extended Moore's Voting Algorithm. At most TWO elements can appear > N/3 times. Track two candidates and two counters.

def majorityElement(nums: list[int]) -> list[int]:
    cnt1, cnt2, el1, el2 = 0, 0, float('-inf'), float('-inf')
    for num in nums:
        if cnt1 == 0 and num != el2:
            cnt1 = 1; el1 = num
        elif cnt2 == 0 and num != el1:
            cnt2 = 1; el2 = num
        elif num == el1:
            cnt1 += 1
        elif num == el2:
            cnt2 += 1
        else:
            cnt1 -= 1; cnt2 -= 1
            
    ans = []
    if nums.count(el1) > len(nums) // 3:
        ans.append(el1)
    if nums.count(el2) > len(nums) // 3:
        ans.append(el2)
    return ans

