# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Extended Boyer-Moore Voting Algorithm. There can be at most 2 elements appearing more than n/3 times. Maintain two candidate elements and their counts.

def majorityElement(nums: List[int]) -> List[int]:
    num1, num2, c1, c2 = -1, -1, 0, 0
    for el in nums:
        if el == num1: c1 += 1
        elif el == num2: c2 += 1
        elif c1 == 0: num1, c1 = el, 1
        elif c2 == 0: num2, c2 = el, 1
        else: c1 -= 1; c2 -= 1
    c1, c2 = 0, 0
    for el in nums:
        if el == num1: c1 += 1
        elif el == num2: c2 += 1
    ans = []
    if c1 > len(nums) // 3: ans.append(num1)
    if c2 > len(nums) // 3: ans.append(num2)
    return ans

